def flatten(mat: list[list | tuple]): # функция "расплющить список"
    if all(type(i) == tuple or type(i) == list for i in mat) == True: return [position_inside for position_outside in range(len(mat)) for position_inside in mat[position_outside]]
    else: return TypeError