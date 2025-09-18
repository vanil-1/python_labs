def is_tuple_list_inside(list_in):
    if all(type(i) == tuple or type(i) == list for i in list_in): return True
    else: return False


def flatten(list_in):
    if is_tuple_list_inside(list_in): 
        return [position_inside for position_outside in range(len(list_in))\
                 for position_inside in list_in[position_outside]]
    else: return TypeError