# MIN_MAX
def min_max(nums: list[float | int]):
    try:  # если существует список -> вывод кортежа вида: (минимальное число списка, максимальное число списка)
        list
        return ((min(nums)), (max(nums)))
    except ValueError:
        return ValueError  # иначе ошибка


min_max_case_list = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]
for case_list in min_max_case_list:
    print(min_max(case_list))
print("-" * 20)


# UNIQUE_SORTED
def unique_sorted(nums: list[float | int]):
    try:  # если существует список -> вывод отсортированного списка с уникальными значениями
        list
        return [number for number in sorted(set(nums))]
    except ValueError:
        return []


unique_sorted_case_list = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0],
]
for case_list in unique_sorted_case_list:
    print(unique_sorted(case_list))
print("-" * 20)


# FLATTEN
def flatten(mat: list[list | tuple]):  # функция "расплющить список"
    if all(type(i) == tuple or type(i) == list for i in mat) == True:
        return [
            position_inside
            for position_outside in range(len(mat))
            for position_inside in mat[position_outside]
        ]
    else:
        return TypeError


flatten_case_list = [
    [[1, 2], [3, 4]],
    ([1, 2], (3, 4, 5)),
    [[1], [], [2, 3]],
    [[1, 2], "ab"],
]
for case_list in flatten_case_list:
    print(flatten(case_list))
print("-" * 20)
