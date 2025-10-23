def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return lens_elements_matrix[0]
    else: return ValueError