from dataclasses import dataclass
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from lib.check_formats.check_date import check_date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        check_date(self.birthdate)
        if not (type(self.gpa) in [float, int] and (0 <= self.gpa <= 5)):
            raise ValueError(
                f"WARNING: gpa must be between 0 and 10, type of gpa must be int or float: {self.gpa}"
            )

    def age(self) -> int:
        birthdate, today = check_date(self.birthdate).year, datetime.today().year
        return today - birthdate

    def to_dict(self) -> dict:
        all_data = [self.fio, self.birthdate, self.group, self.gpa]
        if (
            sum(type(i) == str and i != "" for i in all_data) == 3
            and type(all_data[3]) in [float, int]
        ):
            return {
                "fio": self.fio,
                "birthdate": self.birthdate,
                "group": self.group,
                "gpa": self.gpa,
            }
        else:
            raise ValueError(
                f"WARNING: you must not miss field and type of fio, birtdate and group is str: {all_data}"
            )

    @classmethod
    def from_dict(cls, dict: dict):
        return cls(
            fio=dict["fio"],
            birthdate=dict["birthdate"],
            group=dict["group"],
            gpa=float(dict["gpa"]),
        )

    def __str__(self):
        return f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"


Student1 = Student("Danya", "30.12.2006", "bivt-25-7", 5)

dict_in = {"fio": "Broo", "birthdate": "22.02.2007", "group": "20", "gpa": 4}
Student2 = Student.from_dict(dict_in)

for obj in [Student1, Student2]:
    print(f"str: {obj}")
    print(f"age: {obj.age()}")
    print(f"to_dict: {obj.to_dict()}")
    print("-" * 87)
