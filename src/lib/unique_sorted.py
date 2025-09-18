def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def unique_sorted(list_in):
    try: # если существует список -> вывод отсортированного списка с уникальными значениями
        list
        return [int_float(number) for number in sorted(set(list_in))]
    except ValueError: return []