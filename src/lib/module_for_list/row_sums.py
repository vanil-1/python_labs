from module_for_list.is_matrix import is_matrix


def row_sums(mat: list[list[float | int]]):
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError:
        return [sum(string_matrix) for string_matrix in mat]
    else:
        return ValueError("ValueError: рванная матрица")
