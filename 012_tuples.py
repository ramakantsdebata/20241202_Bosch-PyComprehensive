## Tuples - An immutable form of 'list' type

tp1 = tuple()
tp2 = tuple([1, 2, 3, 4])
tp3 = (1, 2, 3, 4)

tp4 = ()
tp5 = (1,)

print(type(tp1), tp1)
print(type(tp2), tp2)
print(type(tp3), tp3)
print(type(tp4), tp4)
print(type(tp5), tp5)


## NamedTuples
from collections import namedtuple
Point = namedtuple("Point", "x y")
p1 = Point(10, 20)
print(type(p1), p1)

print(p1[0], p1[1])
print(p1.x, p1.y)

# Employee = namedtuple("Employee_cls", ["id", "name", "age"])
Employee = namedtuple("Employee", ["id", "name", "age"])
emp1 = Employee(1, "Rakesh", 25)
print(type(emp1), emp1)
print(emp1.id, emp1.name, emp1.age)
