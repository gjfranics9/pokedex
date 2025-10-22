import json
from pathlib import Path

def load_types(path = "types.txt"):
    p = Path(path)
    if not p.exists():
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f]
