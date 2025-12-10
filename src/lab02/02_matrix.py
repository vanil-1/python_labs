import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib"))
)  # добавляет путь к репозиторию с модулями
import module_for_list.is_matrix as is_matrix  # модуль проверяющий является ли матрица рванной


# TRANSPOSE
def transpose(mat: list[list[float | int]]):
    if mat == []:
        return []
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError:
        return [
            [column_matrix[i] for column_matrix in mat] for i in range(state_of_matrix)
        ]
    elif state_of_matrix == 1:
        return [string_matrix for string_matrix in mat]
    else:
        return ValueError("ValueError: рванная матрица")


transpose_case_mat = [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]
for case_mat in transpose_case_mat:
    print(transpose(case_mat))
print("-" * 20)


# ROW_SUMS
def row_sums(mat: list[list[float | int]]):
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError:
        return [sum(string_matrix) for string_matrix in mat]
    else:
        return ValueError("ValueError: рванная матрица")


row_sums_case_list = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]],
]
for case_mat in row_sums_case_list:
    print(row_sums(case_mat))
print("-" * 20)


# COL_SUMS
def col_sums(mat: list[list[float | int]]):
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError:
        return [
            sum([column_matrix[i] for column_matrix in mat])
            for i in range(state_of_matrix)
        ]
    else:
        return ValueError("ValueError: рванная матрица")


col_sums_case_mat = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]],
]
for case_mat in col_sums_case_mat:
    print(col_sums(case_mat))
print("-" * 20)
