#!/usr/bin/env python3
"""
lore.py — index, search, fetch and validate the Design Lore corpus.

Why this exists: the corpus is ~1000 entries / ~285k tokens across 59 files.
Reading a whole module to find one fact costs 6-16k tokens. INDEX.tsv is one
greppable line per entry, so a lookup is a grep plus a targeted fetch.

  python3 lore.py index                 rebuild INDEX.tsv
  python3 lore.py get fp-012 ms-004     print full entries by id
  python3 lore.py search "focus state"  matching entries (one line each)
  python3 lore.py search "spring" -f title -s figma-prototyping
  python3 lore.py show "reduced motion" print full content of matches
  python3 lore.py validate              schema, id collisions, stale ranges
"""
import argparse
import collections
import glob
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
INDEX = ROOT / "INDEX.tsv"
REQUIRED = ("id", "topic", "title", "content", "tags")
OPTIONAL = ("source", "example", "meta")


def lore_files():
    return sorted(ROOT.glob("skill-*/lore/*.jsonl"))


def load():
    """Yield (entry, skill, relative_path) for every entry in the corpus."""
    for f in lore_files():
        rel = f.relative_to(ROOT).as_posix()
        skill = rel.split("/")[0].removeprefix("skill-")
        for n, line in enumerate(f.read_text().splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line), skill, rel
            except json.JSONDecodeError as e:
                sys.exit(f"{rel}:{n} invalid JSON: {e}")


def cmd_index(args):
    """Write the cross-skill INDEX.tsv plus a per-skill index inside each skill.

    The root index is for working in this repo. The per-skill index ships inside
    the .skill package, so an installed skill can be grepped by title instead of
    read module by module.
    """
    rows, per_skill = [], collections.defaultdict(list)
    for d, skill, rel in load():
        title = d.get("title", "").replace("\t", " ")
        tags = ",".join(d.get("tags", []))
        rows.append("\t".join([d["id"], d["id"].rsplit("-", 1)[0], skill, rel, title, d.get("topic", ""), tags]))
        # inside a skill, the path is relative to the skill root
        per_skill[rel.split("/")[0]].append(
            "\t".join([d["id"], rel.split("/", 1)[1], title, d.get("topic", ""), tags]))

    INDEX.write_text(
        "# Design Lore entry index (all skills) — regenerate with `python3 lore.py index`\n"
        "# id\tprefix\tskill\tfile\ttitle\ttopic\ttags\n"
        + "\n".join(rows) + "\n")
    print(f"wrote {INDEX.name}: {len(rows)} entries, {INDEX.stat().st_size / 1024:.0f} KB")

    for skill_dir, lines in sorted(per_skill.items()):
        out = ROOT / skill_dir / "INDEX.tsv"
        out.write_text(
            f"# {skill_dir} entry index — grep this before reading a module\n"
            "# id\tfile\ttitle\ttopic\ttags\n"
            + "\n".join(lines) + "\n")
        print(f"  {out.relative_to(ROOT)}: {len(lines)} entries, {out.stat().st_size / 1024:.0f} KB")


def _match(d, q, field):
    q = q.lower()
    if field in ("title", "topic"):
        return q in d.get(field, "").lower()
    if field == "tags":
        return any(q in t.lower() for t in d.get("tags", []))
    if field == "content":
        return q in d.get("content", "").lower()
    if field == "meta":
        return q in json.dumps(d.get("meta", {})).lower()
    return (
        q in d.get("title", "").lower()
        or q in d.get("topic", "").lower()
        or q in d.get("content", "").lower()
        or any(q in t.lower() for t in d.get("tags", []))
        or q in json.dumps(d.get("meta", {})).lower()
    )


def _find(query, field, skill):
    for d, sk, rel in load():
        if skill and skill not in sk:
            continue
        if _match(d, query, field):
            yield d, sk, rel


def cmd_search(args):
    n = 0
    for d, sk, rel in _find(args.query, args.field, args.skill):
        n += 1
        print(f"{d['id']:<10} {sk:<20} {d.get('title','')}")
        if n >= args.limit:
            print(f"... (limit {args.limit} reached; narrow with -f or -s)")
            return
    if not n:
        print(f"no match for {args.query!r}"
              + (f" in field '{args.field}'" if args.field != "all" else "")
              + (f" in skill '{args.skill}'" if args.skill else ""))


def _print_entry(d, rel):
    print(f"\n{'=' * 70}\n{d['id']}  [{rel}]\n{d.get('title','')}\n{'-' * 70}")
    if d.get("topic"):
        print(f"topic: {d['topic']}")
    if d.get("tags"):
        print(f"tags:  {', '.join(d['tags'])}")
    if d.get("source"):
        print(f"source: {d['source']}")
    print()
    print(d.get("content", ""))
    if d.get("example"):
        print(f"\nEXAMPLE: {d['example']}")
    if d.get("meta"):
        print(f"\nmeta: {json.dumps(d['meta'], ensure_ascii=False)}")


def cmd_get(args):
    wanted = {i.lower() for i in args.ids}
    found = set()
    for d, sk, rel in load():
        if d["id"].lower() in wanted:
            _print_entry(d, rel)
            found.add(d["id"].lower())
    for miss in wanted - found:
        print(f"\n[not found: {miss}]", file=sys.stderr)


def cmd_show(args):
    n = 0
    for d, sk, rel in _find(args.query, args.field, args.skill):
        _print_entry(d, rel)
        n += 1
        if n >= args.limit:
            print(f"\n... (limit {args.limit} reached)")
            break
    if not n:
        print(f"no match for {args.query!r}")


def cmd_validate(args):
    problems = []
    ids = collections.defaultdict(list)
    prefixes = collections.defaultdict(set)
    bodies = collections.defaultdict(list)
    seen_ranges = collections.defaultdict(list)
    count = 0

    for d, skill, rel in load():
        count += 1
        for k in REQUIRED:
            if k not in d or not d[k]:
                problems.append(f"{rel} {d.get('id','?')}: missing/empty '{k}'")
        for k in d:
            if k not in REQUIRED + OPTIONAL:
                problems.append(f"{rel} {d['id']}: unexpected key '{k}'")
        if not re.fullmatch(r"[a-z]+-\d{3}[a-z]?", d.get("id", "")):
            problems.append(f"{rel} {d['id']}: id should match <prefix>-000")
        if not isinstance(d.get("tags"), list):
            problems.append(f"{rel} {d['id']}: tags must be a list")
        ids[d["id"]].append(rel)
        prefixes[d["id"].rsplit("-", 1)[0]].add(rel)
        num = int(re.search(r"\d+", d["id"]).group())
        seen_ranges[(d["id"].rsplit("-", 1)[0], rel)].append(num)
        bodies[hashlib.md5(d.get("content", "").encode()).hexdigest()].append((rel, d["id"]))

    prefix_ranges = collections.defaultdict(list)
    for (pre, rel), nums in seen_ranges.items():
        prefix_ranges[pre].append((rel, min(nums), max(nums)))

    # An id in two files is fine only when those files mirror each other.
    mirror_pairs = collections.Counter()
    for _, locs in bodies.items():
        if len(locs) > 1:
            mirror_pairs[tuple(sorted({r for r, _ in locs}))] += 1

    for i, locs in ids.items():
        if len(locs) > 1 and tuple(sorted(set(locs))) not in mirror_pairs:
            problems.append(f"id collision (not a mirror): {i} in {', '.join(locs)}")

    # A prefix reused with OVERLAPPING numbers is the collision that bit us
    # before. Sharing a prefix contiguously across sibling modules is fine
    # (al-001..038, al-039..048, al-049..060), so compare ranges, not names.
    for pre, ranges in prefix_ranges.items():
        for i, (fa, lo_a, hi_a) in enumerate(ranges):
            for fb, lo_b, hi_b in ranges[i + 1:]:
                if tuple(sorted((fa, fb))) in mirror_pairs:
                    continue
                if lo_a <= hi_b and lo_b <= hi_a:
                    problems.append(
                        f"prefix '{pre}-' ranges overlap: {fa} ({lo_a:03d}-{hi_a:03d})"
                        f" and {fb} ({lo_b:03d}-{hi_b:03d})")

    # SKILL.md module-index ranges drift as entries are appended.
    for sk in sorted(ROOT.glob("skill-*/SKILL.md")):
        text = sk.read_text()
        base = sk.parent
        for m in re.finditer(r"(lore/[\w\-.]+\.jsonl).*?\|\s*([a-z]+-\d+)\s*(?:→|->)\s*([a-z]+-\d+)", text):
            rel, lo, hi = m.groups()
            path = (base / rel)
            if not path.exists():
                problems.append(f"{sk.relative_to(ROOT)}: indexes missing file {rel}")
                continue
            nums = [int(re.search(r"\d+", json.loads(l)["id"]).group()) for l in path.read_text().splitlines() if l.strip()]
            if (int(re.search(r"\d+", lo).group()), int(re.search(r"\d+", hi).group())) != (min(nums), max(nums)):
                problems.append(
                    f"{sk.relative_to(ROOT)}: {rel} claims {lo}→{hi}, actual {min(nums):03d}→{max(nums):03d}")
        for f in sorted((base / "lore").glob("*.jsonl")):
            if f"lore/{f.name}" not in text:
                problems.append(f"{sk.relative_to(ROOT)}: {f.name} on disk but not in the module index")

    if INDEX.exists():
        indexed = sum(1 for l in INDEX.read_text().splitlines() if l and not l.startswith("#"))
        if indexed != count:
            problems.append(f"INDEX.tsv is stale: {indexed} rows vs {count} entries — run `lore.py index`")
    else:
        problems.append("INDEX.tsv missing — run `lore.py index`")

    per_skill_counts = collections.Counter(rel.split("/")[0] for _, _, rel in load())
    for skill_dir, n in per_skill_counts.items():
        f = ROOT / skill_dir / "INDEX.tsv"
        if not f.exists():
            problems.append(f"{skill_dir}/INDEX.tsv missing — run `lore.py index`")
        else:
            got = sum(1 for l in f.read_text().splitlines() if l and not l.startswith("#"))
            if got != n:
                problems.append(f"{skill_dir}/INDEX.tsv stale: {got} rows vs {n} entries")

    print(f"{count} entries in {len(lore_files())} files")
    if mirror_pairs:
        print("\nmirrored modules (same content in two skills, by design):")
        for files, n in mirror_pairs.most_common():
            print(f"  {n:3} shared  {' <-> '.join(files)}")
    if problems:
        print(f"\n{len(problems)} problems:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nno problems found")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("index", help="rebuild INDEX.tsv").set_defaults(fn=cmd_index)

    g = sub.add_parser("get", help="print full entries by id")
    g.add_argument("ids", nargs="+")
    g.set_defaults(fn=cmd_get)

    for name, fn, helptext in (("search", cmd_search, "list matching entries"),
                               ("show", cmd_show, "print full content of matches")):
        s = sub.add_parser(name, help=helptext)
        s.add_argument("query")
        s.add_argument("-f", "--field", default="all", choices=["all", "title", "topic", "tags", "content", "meta"])
        s.add_argument("-s", "--skill", default=None, help="restrict to skills whose name contains this")
        s.add_argument("-n", "--limit", type=int, default=40 if name == "search" else 5)
        s.set_defaults(fn=fn)

    sub.add_parser("validate", help="check schema, ids, prefixes, SKILL.md ranges").set_defaults(fn=cmd_validate)

    args = ap.parse_args()
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    main()
