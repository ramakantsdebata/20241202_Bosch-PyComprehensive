class CustPointType:
    __slots__ = ['x', 'y']

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f"x[{self.x}], y[{self.y}]"
    
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
