def isinteger(x):
    try:
        int(x)
        return True # if x is integer
    except ValueError: return False # if x isn't integer