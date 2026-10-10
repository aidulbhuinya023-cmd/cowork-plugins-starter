#!/usr/bin/env python3
"""Optional sanity checker for this repo. Standard library only, no install step.

Usage:  python3 scripts/validate.py            # check everything
        python3 scripts/validate.py sales      # check one plugin
"""
import json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
errors, warnings = [], []


def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)


def frontmatter(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data, key = {}, None
    for line in m.group(1).splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            key, _, val = line.partition(":")
            val = val.strip()
            data[key] = "" if val in (">", ">-", "|", "") else val.strip('"')
        elif key and line.startswith("  "):
            data[key] = (data.get(key, "") + " " + line.strip()).strip()
    return data


def check_plugin(d, in_marketplace):
    rel = d.relative_to(REPO)
    pj = d / ".claude-plugin" / "plugin.json"
    if not pj.exists():
        return err(f"{rel}: missing .claude-plugin/plugin.json")
    try:
        meta = json.loads(pj.read_text())
    except json.JSONDecodeError as e:
        return err(f"{rel}: plugin.json is not valid JSON ({e})")
    name = meta.get("name", "")
    if not KEBAB.match(name):
        err(f"{rel}: plugin name '{name}' must be kebab-case")
    if in_marketplace and name != d.name:
        err(f"{rel}: plugin name '{name}' should match folder name '{d.name}'")
    if not SEMVER.match(meta.get("version", "")):
        err(f"{rel}: version must look like 1.2.3")
    if not meta.get("description"):
        err(f"{rel}: plugin.json needs a description")
    for f in ("README.md", "CONNECTORS.md"):
        if not (d / f).exists():
            err(f"{rel}: missing {f}")

    # skills
    skill_names = set()
    for s in sorted((d / "skills").glob("*/")) if (d / "skills").exists() else []:
        sm = s / "SKILL.md"
        if not sm.exists():
            err(f"{rel}/skills/{s.name}: missing SKILL.md")
            continue
        fm = frontmatter(sm)
        if not fm:
            err(f"{sm.relative_to(REPO)}: missing frontmatter")
            continue
        skill_names.add(s.name)
        if fm.get("name") != s.name:
            err(f"{sm.relative_to(REPO)}: name '{fm.get('name')}' must match folder '{s.name}'")
        if len(fm.get("description", "")) < 40:
            err(f"{sm.relative_to(REPO)}: description is missing or too short")
    if not skill_names:
        warn(f"{rel}: no skills found")

    # commands
    for c in sorted((d / "commands").glob("*.md")) if (d / "commands").exists() else []:
        fm = frontmatter(c)
        if not fm or not fm.get("description"):
            err(f"{c.relative_to(REPO)}: command needs a description in frontmatter")
        if not KEBAB.match(c.stem):
            err(f"{c.relative_to(REPO)}: command file name must be kebab-case")
        for ref in re.findall(r"`([a-z0-9-]+)` skill", c.read_text()):
            if ref not in skill_names:
                err(f"{c.relative_to(REPO)}: refers to skill '{ref}' which does not exist")

    # connectors
    mcp = d / ".mcp.json"
    servers = {}
    if mcp.exists():
        try:
            servers = json.loads(mcp.read_text()).get("mcpServers", {})
        except json.JSONDecodeError as e:
            err(f"{rel}/.mcp.json: invalid JSON ({e})")
        for k, v in servers.items():
            if v.get("type") not in ("http", "sse"):
                err(f"{rel}/.mcp.json: server '{k}' needs type http or sse")
            if not str(v.get("url", "")).startswith("https://"):
                err(f"{rel}/.mcp.json: server '{k}' needs an https url")

    # every server in .mcp.json should be described in CONNECTORS.md
    ctext = (d / "CONNECTORS.md").read_text().lower() if (d / "CONNECTORS.md").exists() else ""
    for k in servers:
        if k.split("-")[0] not in ctext:
            warn(f"{rel}: server '{k}' is in .mcp.json but not mentioned in CONNECTORS.md")

    # ~~placeholders used must be defined in CONNECTORS.md
    cm = d / "CONNECTORS.md"
    defined = set(re.findall(r"`(~~[^`]+)`", cm.read_text())) if cm.exists() else set()
    defined.discard("~~category")
    for f in d.rglob("*.md"):
        if f.name == "CONNECTORS.md":
            continue
        for m in re.finditer(r"~~(?=\S)", f.read_text()):
            tail = "~~" + f.read_text()[m.end():m.end() + 40]
            if tail.startswith(("~~category", "~~placeholder")):
                continue  # docs describing the convention itself
            if not any(tail.startswith(p) for p in defined):
                err(f"{f.relative_to(REPO)}: placeholder near '{tail[:20]}' is not defined in CONNECTORS.md")
                break

    # leftover EDIT ME is expected in a starter; just count it
    left = sum(f.read_text().count("EDIT ME") for f in d.rglob("*.md"))
    if left:
        print(f"  note  {rel}: {left} 'EDIT ME' placeholder(s) still to fill in")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    plugin_dirs = sorted(p for p in (REPO / "plugins").glob("*/") if p.is_dir())
    if only:
        plugin_dirs = [p for p in plugin_dirs if p.name == only]
        if not plugin_dirs:
            sys.exit(f"No plugin named '{only}' under plugins/")
    for d in plugin_dirs:
        check_plugin(d, True)
    if not only:
        for d in sorted((REPO / "templates").glob("*/")):
            check_plugin(d, False)
        mp = REPO / ".claude-plugin" / "marketplace.json"
        try:
            market = json.loads(mp.read_text())
        except Exception as e:
            err(f".claude-plugin/marketplace.json: {e}")
            market = {"plugins": []}
        listed = set()
        for entry in market["plugins"]:
            listed.add(entry["name"])
            if not (REPO / entry["source"]).is_dir():
                err(f"marketplace.json: source '{entry['source']}' does not exist")
        for d in plugin_dirs:
            if d.name not in listed:
                err(f"plugins/{d.name} is not listed in .claude-plugin/marketplace.json")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\nChecked {len(plugin_dirs)} plugin(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
