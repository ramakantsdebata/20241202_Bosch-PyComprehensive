class SimpleList:
    def __init__(self, values):
        self.__data__ = list(values)

    def Add(self, data):
        self.__data__.append(data)

    def __getitem__(self, idx):
        return self.__data__[idx]
    
    def __len__(self):
        return len(self.__data__)
    
    def __str__(self):
        return f"{self.__data__}"
    
    def __repr__(self):
        return f"[{type(self)}] --> {self.__data__!r}"
    
    def sort(self):
        self.__data__.sort()

## -------------------------------------------------------------------


class SortedList(SimpleList):
    def __init__(self, values):
        super().__init__(values)
        self.sort()
    
    def Add(self, data):
        super().Add(data)
        self.sort()
    
## -------------------------------------------------------------------


class IntegerList(SimpleList):
    def __init__(self, values):
        data = []
        for val in values:
            # if isinstance(val, int) == False:
            #     raise TypeError("Only accepts integer type elements")
            
            try:
                data.append(int(val))
            except ValueError as ex:
                raise ValueError("Only accepts integer type elements")
            
        super().__init__(data)
    
    def Add(self, data):
        try:
            super().Add(int(data))
        except TypeError as ex:
            raise TypeError("Only accepts integer type elements")
    


#############################################################

def Test1():
    s1 = SimpleList((1, 2, 3, 4, 3, 2, 1))
    print(s1)
    s1.sort()
    print(s1)
    print(">>", s1[1])

    sl1 = SortedList([10, 14, 11, 78, 45, 3])
    print(f"{sl1=}")
    sl1.Add(15)
    print(f"{sl1=}")
    sl1.Add(48)
    print(f"{sl1=}")


    Il1 = IntegerList([1, 2, "10", 3, 4])
    print(Il1)

    try:
        Il2 = IntegerList([1, 2, "Ten"])
    except Exception as ex:
        print(f"{ex!r}")

Test1()
