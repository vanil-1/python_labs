import sys, os, csv, json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
from path_proccesing import path_proccesing, path_is_json, path_is_csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path, csv_path = path_proccesing(json_path, False), path_proccesing(csv_path, True) 
    # path_proccesing(path: str, out: bool), out - если True, создаёт новый файл, иначе файл с исходными данными - создавать не нужно
    
    if not(path_is_json(json_path)):
        with csv_path.open("w", newline = "", encoding = "utf-8") as f_csv, json_path.open(encoding = "utf-8") as f_json:
            rows = json.load(f_json)
            w = csv.DictWriter(f_csv, fieldnames = ['name', 'age'])
            w.writeheader()
            for r in rows: w.writerow(r)

    else: return path_is_json(json_path)
    
print(json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people.csv"))


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path, json_path = path_proccesing(csv_path, False), path_proccesing(json_path, True)
    # path_proccesing(path: str, out: bool), out - если True, создаёт новый файл, иначе файл с исходными данными - создавать не нужно
    
    if not(path_is_csv(csv_path)):
        with json_path.open("w", newline = "", encoding = "utf-8") as f_json, csv_path.open(encoding = "utf-8") as f_csv:
            rows = [{h: h for h in csv.DictReader(f_csv).fieldnames}] + list(csv.DictReader(f_csv))
            json.dump(rows, f_json, ensure_ascii = False, indent = 2)
            
    else: return path_is_csv(csv_path)

print(csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people.json"))



