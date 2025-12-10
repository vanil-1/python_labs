import pytest, sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from lib.json_csv_xlsx.json_csv_xlsx import *


def test_json_to_csv_roundtrip(tmp_path: Path):
    src, dst = tmp_path / "people.json", tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src, dst = tmp_path / "people.csv", tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22, "city": "SPB"},
        {"name": "Bob", "age": 25, "city": "Moscow"},
        {"name": "Carlos", "age": 30, "city": "Kazan"},
        {"name": "Dana", "age": 21, "city": "SPB"},
        {"name": "Andrey", "age": 27, "city": "Novosibirsk"},
    ]

    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(json.load(f))
    assert len(rows) == 5
    assert {"name", "age", "city"} <= set(rows[0].keys())
