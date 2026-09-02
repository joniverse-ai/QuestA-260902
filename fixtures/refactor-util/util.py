import json
from datetime import datetime


def parse_date(s):
    parts = s.split("-")
    if len(parts) != 3:
        return None
    return datetime(int(parts[0]), int(parts[1]), int(parts[2]))


def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def safe_json_load(path):
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
