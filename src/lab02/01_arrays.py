# MIN_MAX
def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def min_max(list_in):
    try: # если существует список -> вывод кортежа вида: (минимальное число списка, максимальное число списка)
        list
        return (int_float(min(list_in)), int_float(max(list_in)))
    except ValueError: return ValueError # иначе ошибка

example_list_01 = list(map(float, input().split())) # переменная для проверки работы функции

print(min_max(example_list_01))

#UNIQUE_SORTED
def int_float(x): # функция для проверки цифры после точки, если есть - число только вещественное, иначе число целое
    if int(x) == x: return int(x)
    else: return x

def unique_sorted(list_in):
    try: # если существует список -> вывод отсортированного списка с уникальными значениями
        list
        return [int_float(number) for number in sorted(set(list_in))]
    except ValueError: return []

example_list_02 = list(map(float, input().split())) # переменная для проверки работы функции

print(unique_sorted(example_list_02))

#FLATTEN
def is_tuple_list_inside(list_in): # функция проверяющая все ли элементы списка/кортежа являются списками/кортежами
    if all(type(i) == tuple or type(i) == list for i in list_in): return True
    else: return False


def flatten(list_in): # функция "расплющить список"
    if is_tuple_list_inside(list_in): return [position_inside for position_outside in range(len(list_in)) for position_inside in list_in[position_outside]]
    else: return TypeError


example_list_03 = [[1, 2], [3, 4]] # примеры для тестирования функции
example_list_04 = ([1, 2], (3, 4, 5)) 
example_list_05 = [[1], [], [2, 3]] 
example_list_06 = [[1, 2], "ab"]
print(flatten(example_list_03))
print(flatten(example_list_04))
print(flatten(example_list_05))
print(flatten(example_list_06))



