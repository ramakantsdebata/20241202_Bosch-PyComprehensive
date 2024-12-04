def addWhole(a, b):
    """
    addWhole(int, int) -> int
    The input should be whole numbers only 
    i.e. 0 or greater"""
    if a < 0 or b < 0:
        print(addWhole.__doc__)
        return
    return a + b


print(addWhole(-1, 2))
print(addWhole(1, 2))
