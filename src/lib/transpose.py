from is_matrix import is_matrix

def transpose(mat: list[list[float | int]]):
    if mat == []: return []
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError: return [[column_matrix[i] for column_matrix in mat] for i in range(state_of_matrix)]
    elif state_of_matrix == 1: return [string_matrix for string_matrix in mat]
    else: return ValueError('ValueError: рванная матрица')