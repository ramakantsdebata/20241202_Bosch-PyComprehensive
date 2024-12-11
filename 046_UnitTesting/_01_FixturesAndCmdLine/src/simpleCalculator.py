class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def add2(self, a, b):
        return a + b


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    obj = Calculator(a, b)

    choice = None

    while choice != 0:
        print("1. Add")
        print("2. Sub")
        print("3. Mul")
        print("4. Div")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("Result = ", obj.add())
            case 2:
                print("Result = ", obj.sub())
            case 3:
                print("Result = ", obj.mul())
            case 4:
                print("Result = ", obj.div())
            case 0:
                break
            case _:
                print("\nPlease provide a valid input\n")


