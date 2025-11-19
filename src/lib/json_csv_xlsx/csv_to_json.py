import csv, json
from pathlib import Path

def path_proccesing(path_str: str, out: bool):
    path = Path(path_str)
    if out: path.parent.mkdir(parents = True, exist_ok = True)
    return path
def path_is_json(path: Path, error = None):
    if path.exists():
        if path.suffix.lower() == ".json": error = False
        else: error = ValueError
    else: error = FileNotFoundError
    return error
def path_is_csv(path: Path, error = None):
    if path.exists():
        if path.suffix.lower() == ".csv": error = False
        else: error = ValueError
    else: error = FileNotFoundError
    return error

def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path, json_path = path_proccesing(csv_path, False), path_proccesing(json_path, True)
    if not(path_is_csv(csv_path)):
        with json_path.open("w", newline = "", encoding = "utf-8") as f_json, csv_path.open(encoding = "utf-8") as f_csv:
            read_csv = csv.DictReader(f_csv)
            rows = [{headers: headers for headers in read_csv.fieldnames}] + list(read_csv)
            json.dump(rows, f_json, ensure_ascii = False, indent = 2)
    else: return path_is_csv(csv_path)