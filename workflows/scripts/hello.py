import os
from datetime import datetime, timezone

name = os.getenv("NAME", "Argo")

print(f"Hello {name}!")
print(f"Executed at: {datetime.now(timezone.utc).isoformat()}")
print("Python script executed successfully.")