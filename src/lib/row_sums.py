def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return True
    else: return False

def row_sums(matrix_in): 
    state_of_matrix = is_matrix(matrix_in)
    if state_of_matrix == True: return [sum(string_matrix) for string_matrix in matrix_in]
    else: return ValueError('ValueError: рванная матрица')