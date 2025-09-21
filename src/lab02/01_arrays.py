# MIN_MAX
def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def min_max(list_in):
    try: # если существует список -> вывод кортежа вида: (минимальное число списка, максимальное число списка)
        list
        return (int_float(min(list_in)), int_float(max(list_in)))
    except ValueError: return ValueError # иначе ошибка

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42])) 
print(min_max([-5, -2, -9]))
print(min_max([])) 
print(min_max([1.5, 2, 2.0, -3.1])) 

#UNIQUE_SORTED
def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def unique_sorted(list_in):
    try: # если существует список -> вывод отсортированного списка с уникальными значениями
        list
        return [int_float(number) for number in sorted(set(list_in))]
    except ValueError: return []

print(unique_sorted([3, 1, 2, 1, 3])) 
print(([])) # []
print(unique_sorted([-1, -1, 0, 2, 2])) 
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 

#FLATTEN
def is_tuple_list_inside(list_in): # функция проверяющая все ли элементы списка/кортежа являются списками/кортежами
    if all(type(i) == tuple or type(i) == list for i in list_in): return True
    else: return False


def flatten(list_in): # функция "расплющить список"
    if is_tuple_list_inside(list_in): return [position_inside for position_outside in range(len(list_in)) for position_inside in list_in[position_outside]]
    else: return TypeError

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5)) ))
print(flatten([[1], [], [2, 3]] ))
print(flatten([[1, 2], "ab"]))