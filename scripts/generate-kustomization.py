from pathlib import Path
import re

path = Path("workflows/kustomization.yaml")
content = path.read_text()

files = sorted(Path("workflows/scripts").glob("*.py"))

match = re.search(r"^(\s*)files:\s*\n(?:[ \t]+-[^\n]*\n)*", content, re.MULTILINE)

if not match:
    raise ValueError("Cannot find configMapGenerator.files")

indent = match.group(1)
entries = "".join(
    f"{indent}  - scripts/{p.name}\n" for p in files
)

updated = content[:match.start()] + f"{indent}files:\n{entries}" + content[match.end():]
path.write_text(updated)