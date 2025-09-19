# TRANSPOSE
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

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

# ROW_SUMS
def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return True
    else: return False

def row_sums(matrix_in): 
    state_of_matrix = is_matrix(matrix_in)
    if state_of_matrix == True: return [sum(string_matrix) for string_matrix in matrix_in]
    else: return ValueError('ValueError: рванная матрица')

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

# COL_SUMS
def is_matrix(matrix_in): # проверка является ли матрица рванной
    lens_elements_matrix = [len(element) for element in matrix_in]
    if min(lens_elements_matrix) == max(lens_elements_matrix): return lens_elements_matrix[0]
    else: return False

def col_sums(matrix_in):
    state_of_matrix = is_matrix(matrix_in)
    if state_of_matrix != False: return [sum([column_matrix[i] for column_matrix in matrix_in]) for i in range(state_of_matrix)]
    else: return ValueError("ValueError: рванная матрица")

print(col_sums([[1, 2, 3], [4, 5, 6]])) # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]])) # [9, -9]
print(col_sums([[0, 0], [0, 0]])) # [0, 0]
print(col_sums([[1, 2], [3]])) # ValueError (рваная)