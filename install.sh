#!/usr/bin/env bash
#
# install.sh — make every skill in this repo available to Claude Code.
#
# Symlinks each skill directory into ~/.claude/skills/ using the name from its
# SKILL.md frontmatter. Nothing is copied, so `git pull` is all it takes to get
# updates — there is no installed copy that can go stale.
#
#   ./install.sh              install (or refresh) all skills
#   ./install.sh --list       show what would be linked, change nothing
#   ./install.sh --uninstall  remove only the links this repo created
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HOME}/.claude/skills"
MODE="${1:-install}"

command -v python3 >/dev/null 2>&1 || { echo "error: python3 is required" >&2; exit 1; }

# name<TAB>directory, read from each SKILL.md's frontmatter
skill_map() {
  python3 - "$REPO" <<'PY'
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
for f in sorted(root.glob("skill-*/SKILL.md")):
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        print(f"WARN\t{f.parent.name}\tno frontmatter", file=sys.stderr); continue
    name = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
    print(f"{(name.group(1) if name else f.parent.name)}\t{f.parent.name}")
PY
}

case "$MODE" in
  --list)
    printf '%-28s %s\n' "SKILL NAME" "DIRECTORY"
    skill_map | while IFS=$'\t' read -r name dir; do printf '%-28s %s\n' "$name" "$dir"; done
    exit 0
    ;;
  --uninstall)
    n=0
    while IFS=$'\t' read -r name dir; do
      link="$DEST/$name"
      # only remove a symlink that points into THIS repo
      if [ -L "$link" ] && [[ "$(readlink "$link")" == "$REPO"/* ]]; then
        rm "$link"; echo "removed  $name"; n=$((n+1))
      fi
    done < <(skill_map)
    echo "removed $n link(s); repo untouched"
    exit 0
    ;;
  install) ;;
  *) echo "usage: $0 [--list|--uninstall]" >&2; exit 2 ;;
esac

mkdir -p "$DEST"
linked=0; skipped=0

while IFS=$'\t' read -r name dir; do
  link="$DEST/$name"

  # ~/.claude/skills/synced/ is reserved by Claude Code for claude.ai skills
  if [ "$(printf '%s' "$name" | tr '[:upper:]' '[:lower:]')" = "synced" ]; then
    echo "SKIP  $name — 'synced' is reserved by Claude Code"; skipped=$((skipped+1)); continue
  fi

  # never clobber a real directory or a link owned by something else
  if [ -e "$link" ] && [ ! -L "$link" ]; then
    echo "SKIP  $name — a real directory already exists at $link"; skipped=$((skipped+1)); continue
  fi
  if [ -L "$link" ] && [[ "$(readlink "$link")" != "$REPO"/* ]]; then
    echo "SKIP  $name — already linked elsewhere: $(readlink "$link")"; skipped=$((skipped+1)); continue
  fi

  ln -sfn "$REPO/$dir" "$link"
  [ -f "$link/SKILL.md" ] || { echo "FAIL  $name — SKILL.md not readable through the link"; skipped=$((skipped+1)); continue; }
  printf 'linked   %-28s -> %s\n' "$name" "$dir"; linked=$((linked+1))
done < <(skill_map)

echo
echo "$linked skill(s) linked into $DEST${skipped:+, $skipped skipped}"
echo "Restart Claude Code (or start a new session) to pick them up."
echo "To update later: git pull — the links follow the repo, nothing to reinstall."
