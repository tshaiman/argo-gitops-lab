from pathlib import Path

path = Path("workflows/kustomization.yaml")
content = path.read_text()

start = content.index("    files:")
end = content.index("\ngeneratorOptions:", start)

files = sorted(Path("workflows/scripts").glob("*.py"))
entries = "\n".join(f"      - scripts/{p.name}" for p in files)

updated = content[:start] + "    files:\n" + entries + "\n" + content[end:]
path.write_text(updated)