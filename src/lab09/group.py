import csv, sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from lib.classes.model_student import Student
from lib.pathProccesing import inicialPath


class Group:
    storage_path: str
    find_students = []

    def __init__(self, storage_path: str):
        self.storage_path = inicialPath(storage_path, ".csv")
        with self.storage_path.open(encoding="utf-8") as f:
            w = csv.DictReader(f)
            if w.fieldnames == ["fio", "birthdate", "group", "gpa"]:
                pass
            else:
                raise ValueError("CSV file does not have fieldnames!")

    def _read_all(self):
        with self.storage_path.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        return rows

    def list(self):
        rows = Group._read_all(self)
        list_student = [
            Student(st["fio"], st["birthdate"], st["group"], float(st["gpa"]))
            for st in rows
        ]
        return list_student

    def add(self, student: Student):
        rows, student_dict = Group._read_all(self), student.to_dict()
        student_dict["gpa"] = str(student_dict["gpa"])
        if sum(student_dict == st for st in rows) == 0:
            with self.storage_path.open("a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                w.writerow(student_dict)
            return "Student is added succsesful!"
        else:
            return "Student in CSV!"

    def find(self, Student: Student):
        rows = Group._read_all(self)
        return [r for r in rows if Student.fio in r["fio"]]

    def remove(self, Student: Student):
        rows = Group._read_all(self)
        if Group.find(self, Student.fio) != []:
            for i, row in enumerate(rows):
                if row["fio"] == Student.fio:
                    rows.pop(i)
                    break
            with self.storage_path.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                w.writeheader()
                w.writerows(rows)
            return "Succesful remove!"
        else:
            return "Do not match Student"

    def update(self, fio: str, Student: Student):
        rows = Group._read_all(self)
        if Group.find(self, fio) != []:
            for i, row in enumerate(rows):
                if row["fio"] == fio:
                    rows.pop(i)
                    rows.insert(
                        i,
                        {
                            "fio": Student.fio if Student.fio != "" else row["fio"],
                            "birthdate": (
                                Student.birthdate
                                if Student.birthdate != ""
                                else row["birthdate"]
                            ),
                            "group": (
                                Student.group if Student.group != "" else row["group"]
                            ),
                            "gpa": Student.gpa if Student.gpa != "" else row["gpa"],
                        },
                    )
                    break
            with self.storage_path.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                w.writeheader()
                w.writerows(rows)
            return "Succesful update!"
        else:
            return "Do not match Student"

    def stats(self):
        rows = Group._read_all(self)
        rows_gpa = [float(gpa["gpa"]) for gpa in rows]

        groups_uniq = set([group["group"] for group in rows])
        group_uniq_count = {
            group: len([x for x in rows if x["group"] == group])
            for group in groups_uniq
        }

        top_student = [{"fio": st["fio"], "gpa": float(st["gpa"])} for st in rows]
        top_5_student_sorted = sorted(top_student, key=lambda x: -x["gpa"])

        student_stats = {
            "count": len(rows_gpa),
            "min_gpa": min(rows_gpa),
            "max_gpa": max(rows_gpa),
            "avg_gpa": (sum(rows_gpa) / len(rows_gpa)),
            "groups": group_uniq_count,
            "top_5_students": top_5_student_sorted[:5],
        }
        return student_stats


path_to_group = Group("data/lab09/students.csv")

print(path_to_group)
# print(path_to_group.stats())
# for rows in path_to_group._read_all():
# print(rows)

# for el in path_to_group.list():
# print(el)

# new_student = Student('misha', '30.12.2006', 'BIVT-25-7', 3)
# ffind_student = "Danwefa"
# update_student = Student("Michail", "12.10.1999", "rock", 2)
# print(path_to_group.add(new_student))
# print(path_to_group.find(new_student))
# print(path_to_group.remove(new_student))
# print(path_to_group.update("misha", update_student))
