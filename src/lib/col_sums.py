def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return lens_elements_matrix[0]
    else: return False

def col_sums(matrix_in):
    state_of_matrix = is_matrix(matrix_in)
    if state_of_matrix != False: return [sum([column_matrix[i] for column_matrix in matrix_in]) for i in range(state_of_matrix)]
    else: return ValueError("ValueError: рванная матрица")