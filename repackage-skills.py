#!/usr/bin/env python3
"""
Auto-repackage skill .skill file when lore files or SKILL.md change.
Called by Claude Code PostToolUse hook — reads hook JSON from stdin.
"""
import fnmatch
import json
import pathlib
import sys
import zipfile

PROJECT = pathlib.Path("/Users/andermagri/Documents/GitHub/Skill-stack")

SKILL_DIRS = {
    "skill-design":           PROJECT / "skill-design",
    "skill-design-system":    PROJECT / "skill-design-system",
    "skill-figma":            PROJECT / "skill-figma",
    "skill-figma-autolayout": PROJECT / "skill-figma-autolayout",
    "skill-industry":         PROJECT / "skill-industry",
    "skill-psychology":       PROJECT / "skill-psychology",
    "skill-builder-frontend": PROJECT / "skill-builder-frontend",
    "skill-builder-fde":      PROJECT / "skill-builder-fde",
}

EXCLUDE_FILES = {".DS_Store"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_DIRS  = {"__pycache__", "node_modules", "evals"}


def should_exclude(rel: pathlib.Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    name = rel.name
    if name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(name, p) for p in EXCLUDE_GLOBS)


def package_skill(skill_path: pathlib.Path) -> pathlib.Path:
    out = PROJECT / f"{skill_path.name}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(skill_path.rglob("*")):
            if not f.is_file():
                continue
            arcname = f.relative_to(skill_path.parent)
            if should_exclude(arcname):
                continue
            zf.write(f, arcname)
    return out


def main():
    # Read hook payload from stdin
    try:
        data = json.load(sys.stdin)
        file_path = data.get("tool_input", {}).get("file_path", "")
    except Exception:
        file_path = ""

    if not file_path:
        sys.exit(0)

    # Only act on .jsonl or SKILL.md files inside a known skill dir
    p = pathlib.Path(file_path)
    if p.suffix not in (".jsonl", ".md") and p.name != "SKILL.md":
        sys.exit(0)

    packaged_any = False
    for skill_name, skill_dir in SKILL_DIRS.items():
        try:
            p.relative_to(skill_dir)          # raises if not inside this dir
        except ValueError:
            continue
        out = package_skill(skill_dir)
        print(json.dumps({
            "systemMessage": f"📦 {skill_name}.skill updated — ready to upload"
        }))
        packaged_any = True

    if not packaged_any:
        sys.exit(0)


if __name__ == "__main__":
    main()
