import re
import sys


def parse_errors(log_path: str) -> list[dict]:
    pattern = re.compile(
        r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ERROR \[(\w+)\] (.+)$"
    )
    errors = []
    with open(log_path) as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                errors.append({
                    "time": m.group(1),
                    "module": m.group(2),
                    "message": m.group(3),
                })
    return errors


def to_markdown_table(errors: list[dict]) -> str:
    lines = ["| 시간 | 모듈 | 메시지 |", "|------|------|--------|"]
    for e in errors:
        lines.append(f"| {e['time']} | {e['module']} | {e['message']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.log"
    errors = parse_errors(path)
    print(to_markdown_table(errors))
