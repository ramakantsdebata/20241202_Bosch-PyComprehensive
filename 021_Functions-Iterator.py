class FibGen:
    def __init__(self, limit) -> None:
        self.limit = limit

    def __iter__(self):
        self.counter = 0
        self.a, self.b = 0, 1
        return self

    def __next__(self):
        if self.counter < self.limit: 
            temp = self.a
            self.a, self.b = self.b, self.a + self.b
            self.counter += 1
            return temp
        else:
            raise StopIteration



#------------------------------


def Main():
    obj = FibGen(10)        # Generate 10 numbers from the series


    it = iter(obj)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

    print("-"*80, "\n")

    for val in obj:
        print(val, end=", ")
    print("\n")

    for val in obj:
        print(val, end=", ")
    print("\n")

Main()