import os
from datetime import datetime, timezone

name = os.getenv("NAME", "Argo")

print(f"validation {name}!")