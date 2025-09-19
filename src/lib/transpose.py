def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return lens_elements_matrix[0]
    else: return ValueError

def transpose(matrix_in):
    if matrix_in == []: return []
    state_of_matrix = is_matrix(matrix_in)
    if state_of_matrix != ValueError: return [[column_matrix[i] for column_matrix in matrix_in] for i in range(state_of_matrix)]
    elif state_of_matrix == 1: return [string_matrix for string_matrix in matrix_in]
    else: return ValueError('ValueError: рванная матрица')