def tuples(fio, group, gpa):
    if fio != '' and group != '' and type(gpa) == float:
        list_fio = [i for i in fio.split()]
        initials_io = [str(i)[0].upper() + '.' for i in list_fio[1:]]
        return f'{list_fio[0][0].upper() + list_fio[0][1:]} {''.join(initials_io)}, гр. {group}, GPA {"{:.2f}".format(gpa)}'
    elif type(gpa) != float: return TypeError
    elif fio != '' and group != ''and type(gpa) != float: return ValueError and TypeError
    else: return ValueError