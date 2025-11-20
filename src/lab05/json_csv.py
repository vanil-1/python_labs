import sys, os, csv, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))
from pathProccesing import pathProccesing

def json_to_csv(json_path: str, csv_path: str, path_suffix = ('.json', '.csv')) -> None:
    json_path, csv_path = pathProccesing(json_path, False, path_suffix), pathProccesing(csv_path, True, path_suffix) 
    if json_path:
        with csv_path.open("w", newline = "", encoding = "utf-8") as f_csv, json_path.open(encoding = "utf-8") as f_json:
            rows = json.load(f_json)
            w = csv.DictWriter(f_csv, fieldnames = list(rows[0].keys()))
            w.writeheader()
            for r in rows: w.writerow(r)
    else: return json_path

def csv_to_json(csv_path: str, json_path: str, path_suffix = ('.json', '.csv')) -> None:
    csv_path, json_path = pathProccesing(csv_path, False, path_suffix), pathProccesing(json_path, True, path_suffix)
    if csv_path:
        with json_path.open("w", newline = "", encoding = "utf-8") as f_json, csv_path.open(encoding = "utf-8") as f_csv:
            read_csv = csv.DictReader(f_csv)
            rows = [{headers: headers for headers in read_csv.fieldnames}] + list(read_csv)
            json.dump(rows, f_json, ensure_ascii = False, indent = 2)
    else: return csv_path

json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json ")