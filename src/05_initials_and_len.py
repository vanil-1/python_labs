surname, name, patronymic = map(str, input('ФИО: ').split())
print(f'Инициалы: {surname[0] + name[0] + patronymic[0]}\n\
Длина (символов): {len(surname + name + patronymic) + 2}')