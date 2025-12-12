import sys, json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from lib.pathProccesing import pathProccesing
from lib.classes.model_student import Student


def students_to_json(students, path):
    path = pathProccesing(path, True, path_suffix=".json")
    data = [Student(st[0], st[1], st[2], st[3]).to_dict() for st in students]
    json.dumps(data, ensure_ascii=False, indent=2)
    with path.open("w", newline="", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path) -> list:
    path = pathProccesing(path, False, path_suffix=".json")
    students = json.load(path.open(encoding="utf-8"))
    return students


students = [
    ("Иванов Иван Иванович", "20/11/2000", "ABCD", 4.5),
    ("Петров Пётр Петрович", "05.03.1999", "XYZ", 3),
    ("Сидоров Сидор Сидорович", "2001/12/31", "QWE", 5),
    ("Алексеева Анна Сергеевна", "1998.07.15", "RTY", 0.0),
    ("Brown Bob", "01/01/2005", "GHJK", 2.7),
    ("Smith John", "14.09.2003", "KLM", 1),
    ("Johnson Kate", "2010/04/09", "POI", 4.8),
    ("Williams Mark", "1995.02.28", "BNM", 3.9),
]

students_to_json(students, "data/lab08/out/students_to_json.json")
for i in students_from_json("data/lab08/samples/students_to_json.json"):
    print(i)
