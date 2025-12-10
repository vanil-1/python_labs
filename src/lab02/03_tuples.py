def tuples(rec: tuple[str, str, float]):
    fio, group, gpa = rec[0], rec[1], rec[2]
    if fio != "" and group != "" and type(gpa) == float:
        list_fio = [i for i in fio.split()]
        initials_io = [str(i)[0].upper() + "." for i in list_fio[1:]]
        return f'{list_fio[0][0].upper() + list_fio[0][1:]} {''.join(initials_io)}, гр. {group}, GPA {"{:.2f}".format(gpa)}'
    elif type(gpa) != float:
        return TypeError
    elif fio != "" and group != "" and type(gpa) != float:
        return ValueError and TypeError
    else:
        return ValueError


tuple_case_tuples = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
]
for case_tuples in tuple_case_tuples:
    print(tuples(case_tuples))
