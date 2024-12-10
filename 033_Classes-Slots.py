class CustPointType:
    __slots__ = ['x', 'y']

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f"x[{self.x}], y[{self.y}]"
    
    def __del__(self):
        print("__del__ Deleting the object")

    def __delattr__(self, name):
        print(f"__delattr__ Deleting the attribute {type(name)} --> {name}")
        raise AttributeError("Deleting attributes not permitted")
    
def Test1():
    p1 = CustPointType(1, 2)
    print(p1)

    try:
        p1.z = 3        # Can't add attributes
    except AttributeError as ex:
        print(f"EXCEPTION --> {ex!r}")


    try:
        del p1.x
    except AttributeError as ex:
        print(f"EXCEPTION --> {ex!r}")

    # print(p1)


def Test2():
    p1 = CustPointType(1, 2)
    p2 = CustPointType(3, 4)


    del p1
    try:
        del p2.x
    except AttributeError as ex:
        print(f"{ex!r}")

    print(p2.x)
    print("Exiting the method")

Test2()
