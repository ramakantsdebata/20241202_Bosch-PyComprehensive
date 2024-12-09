class Integer:
    def __init__(self, data = 0):
        self.data = data

    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):
        return Integer(self.data +  other.data)
    

i1 = Integer(10)
i2 = Integer(20)

i3 = i1 + i2

print(type(i3), i3)