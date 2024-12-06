class Shape:
    def Draw(self):
        pass

    def Area(self):
        pass

    def Peri(self):
        pass

class Rhombus:
    pass

class Square(Rhombus):
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def Draw(self):
        print("Drawing a square...")

    def Area(self):
        return self.side **2

    def Peri(self):
        return 4 * self.side


class Circle:
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def Draw(self):
        print("Drawing a circle...")

    def Area(self):
        PI = 22/7
        return PI * self.radius **2

    def Peri(self):
        PI = 22/7
        return 2 * PI * self.radius


def PrintArea(sh:Shape):
    area = sh.Area()
    print(f"{sh.__class__.__name__} --> {area}")

if __name__ == "__main__":
    sh = Shape()
    sq = Square(10)
    cr = Circle(10)

    PrintArea(sh)
    PrintArea(sq)
    PrintArea(cr)


