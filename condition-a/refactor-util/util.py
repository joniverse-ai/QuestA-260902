import json
from datetime import datetime
from typing import Any, Optional


def parse_date(s: str) -> Optional[datetime]:
    """Parse 'YYYY-MM-DD' string into a datetime, returning None on failure."""
    parts = s.split("-")
    if len(parts) != 3:
        return None
    return datetime(int(parts[0]), int(parts[1]), int(parts[2]))


def flatten(nested: list) -> list:
    """Recursively flatten a nested list into a single-level list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def safe_json_load(path: str) -> dict[str, Any]:
    """Load JSON from a file path, returning an empty dict on any error."""
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
