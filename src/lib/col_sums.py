from is_matrix import is_matrix

def col_sums(mat: list[list[float | int]]):
    state_of_matrix = is_matrix.is_matrix(mat)
    if state_of_matrix != ValueError: return [sum([column_matrix[i] for column_matrix in mat]) for i in range(state_of_matrix)]
    else: return ValueError("ValueError: рванная матрица")