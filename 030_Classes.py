from random import randint

class Car:
    carCounter = 0  # Class Attribute

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.__color = color
        self.chasisNo = Car.GenChasisNo() + "-" + str(Car.carCounter)
        self.bRunning = False
        self.__velocity = 0

        # self.carCount = 1
        # global carCounter
        Car.carCounter += 1

        # print(Car.carCounter)
        # print(">>", self.carCounter)

        self.lastServiceDate = 0

    def __del__(self):
        print(f"Deleting the object [{self.__class__.__name__} at {id(self)}]")
        Car.carCounter -= 1

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.__color}, {self.__velocity}"
    
    def __repr__(self):
        return f"[{Car.carCounter}] {self.make}, {self.model}, {self.year}, {self.__color}, [{self.chasisNo}], [Serviced on {self.lastServiceDate}], {self.bRunning=}"
    
    @classmethod
    def GetCarCount(cls):
        # print(">>>", cls)
        return cls.carCounter

    @staticmethod
    def GenChasisNo():
        return "Car_" + str(randint(1, 1000))
    
    @staticmethod
    def GetAttributions():
        return f"Inspired by Ferrari"
    
    @staticmethod
    def About():
        return f"This is a family centric vehicle to ensure economy as well as safety"

    def Start(self):
        if self.bRunning == False:
            self.startCount = 1
            print(f"Starting the {self.__color} {self.model}...")
            self.bRunning = True
        else:
            self.startCount += 1
            print("Car is already running. Avoid pressing the starter needlessly")

    def Stop(self):
        if self.bRunning == True:
            self.startCount = 0
            print(f"Stopping the {self.__color} {self.model}...")
            self.bRunning = False
        else:
            print("Car is not running.")

    # def Display(self):
    #     print(self.prepString())

    def Accelerate(self, velocity):
        if self.bRunning == True and self.__velocity < velocity:
            self.__velocity = velocity
            return 
        raise ValueError("Cannot accelerate to a lower or equal speed")
        

    def Decelerate(self, velocity):
        if self.bRunning == True and self.__velocity > velocity:
            self.__velocity = velocity
        raise ValueError("Cannot decelerate to a higher or equal speed")

    @property
    def Velocity(self):
        return self.__velocity

    @property
    def Color(self):
        return self.__color
    
    @Color.setter
    def Color(self, color):
        print(f"Setting color to {color} ...")
        self.__color = color

    @property
    def Model(self):
        return self.model
    
    @property
    def ServiceDate(self):
        # pass
        raise NotImplemented("Fetching this data is not permitted")
    
    @ServiceDate.setter
    def ServiceDate(self, today):
        self.lastServiceDate = today



##----------------------------------------------------------------------------------

class GearedCar(Car):
    def __init__(self, gears, *vArgs, **kwArgs):
        super().__init__(*vArgs, **kwArgs)
        self.gears = gears
        self.gearState = 0

    # def ShiftUp(self, value):
    #     self.gearState = value

    # def ShiftDown(self, value):
    #     self.gearState = value

    @property
    def GearState(self):
        raise NotImplemented
    
    @GearState.setter
    def GearState(self, value):
        if value < 0 or value > self.gears:
            raise ValueError(f"Car has only {self.gears} gears.")
        
        self.gearState = value

    def Stop(self):
        if self.gearState != 0:
            raise ValueError("Gear should be in neutral (0) before stopping the car.")
        super().Stop()

    def __gt__(self, other):
        return self.gears > other.gears

###############################################################

def Test1():
    c1 = Car("Honda", "Accord", 2024, "Black")
    # c1.Display()
    # print(c1.toString())

    print(c1)
    print(c1.__str__())
    print(c1.__repr__())
    print(str(c1))

    data = str(c1)

    c1.Start()
    c1.Stop()


def Test2():
    # print(f"We have {Car.GetCarCount()} cars created!")
    
    c1 = Car("Honda", "Accord", 2024, "Black")
    print(f"[{Car.carCounter}]")
    c2 = Car("Toyota", "Camry", 2023, "Yellow")
    print(f"[{c1.carCounter}]")

    c1.Start(); print(c1.startCount)
    c1.Start(); print(c1.startCount)
    c1.Start(); print(c1.startCount)
    c1.Start(); print(c1.startCount)


    c1.Stop(); print(c1.startCount)
    c1.Start(); print(c1.startCount)
    c1.Start(); print(c1.startCount)
    c1.Start(); print(c1.startCount)

    print(c1)
    print(f"{c1!r}")
    print(f"We have {c1.GetCarCount()} cars created!")

def Test3():
    c1 = Car("Honda", "Accord", 2024, "Black")
    c2 = Car("Toyota", "Camry", 2023, "Yellow")

    print(repr(c1))
    print(repr(c2))
    print(Car.About())
    print(Car.GetAttributions())

    c1.Start()
    c1.Accelerate(10)

    print(dir(c1))
    print(c1)
    # print(c1.__velocity)
    c1._Car__velocity = 200
    print(c1._Car__velocity)
    print(dir(c1))
    print(c1)
    print(f"Velocity --> {c1.GetVelocity()}")

def Test4():
    c1 = Car("Honda", "Accord", 2024, "Black")
    c2 = Car("Toyota", "Camry", 2023, "Yellow")

    # print(c1.GetColor())
    # c1.SetColor("Red")
    # print(c1.GetColor())

    print(c1.Color)
    c1.Color = "Blue"
    print(c1.Color)

    c1.ServiceDate = 2023
    print(repr(c1))
    # print(c1.ServiceDate)

def Test5():
    c1 = GearedCar(5, "Honda", "Accord", 2024, "Black")
    c2 = GearedCar(7, "Toyota", "Camry", 2023, "Yellow")

    c1.Start()
    c1.GearState = 3
    c1.GearState = 0
    c1.Stop()
    print(repr(c1))

def Test6():
    c1 = GearedCar(5, "Honda", "Accord", 2024, "Black")
    c2 = GearedCar(7, "Toyota", "Camry", 2023, "Yellow")

    # if c1 > c2:
    if c1.__gt__(c2):
        print(f"{c1.Color}-{c1.Model} is better than {c2.Color}-{c2.Model}")
    else:
        print(f"{c2.Color}-{c2.Model} is better than {c1.Color}-{c1.Model}")

def Test7():
    c1 = GearedCar(5, "Honda", "Accord", 2024, "Black")
    c2 = GearedCar(7, "Toyota", "Camry", 2023, "Yellow")
    c3 = GearedCar(5, "Hyundai", "Accent", 2023, "Yellow")


    print(Car.GetCarCount())

    del c1

    print(Car.GetCarCount())

def Test8():
    c1 = GearedCar(5, "Honda", "Accord", 2024, "Black")
    for member in dir(c1):
        print(member)

    print("\n" + "*"* 40 + "\n")

    for member in c1.__dict__:
        print(member)

def Test9():
    c1 = GearedCar(5, "Honda", "Accord", 2024, "Black")
    for member in c1.__dict__:
        print(member)

    print("\n" + "*"* 40 + "\n")

    del c1.chasisNo
    # del c1.__dict__["chasisNo"]

    c1.newAttrib = "SomeState"
    for member in c1.__dict__:
        print(member)


if __name__ == "__main__":
    Test9()