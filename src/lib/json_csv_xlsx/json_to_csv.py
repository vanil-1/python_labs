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

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path, csv_path = path_proccesing(json_path, False), path_proccesing(csv_path, True) 
    if not(path_is_json(json_path)):
        with csv_path.open("w", newline = "", encoding = "utf-8") as f_csv, json_path.open(encoding = "utf-8") as f_json:
            rows = json.load(f_json)
            w = csv.DictWriter(f_csv, fieldnames = list(rows[0].keys()))
            w.writeheader()
            for r in rows: w.writerow(r)
    else: return path_is_json(json_path)