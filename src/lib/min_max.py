def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def min_max(list_in):
    try: # если существует список -> вывод кортежа вида: (минимальное число списка, максимальное число списка)
        list
        return (int_float(min(list_in)), int_float(max(list_in)))
    except ValueError: return ValueError # иначе ошибка