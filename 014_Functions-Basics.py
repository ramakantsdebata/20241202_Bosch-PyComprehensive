#region Define Earlier vs. Declare Higher

# def Bar():
#     print("Bar")
#     Baz()

# def Baz():
#     print("Baz")

# def Foo():
#     print("Foo")
#     Bar()

# def Main():
#     print("Main")
#     Foo()

# Main()

#endregion


#region Argument Passing
## Positional args ######################################
# def add(*, a=0, b):
#     print(f"{a=}, {b=}")
#     return a+b


# print(add(1, 2))
# print(add(b=1))


## Keyworded args #####################################
# print(add(a=1, b=2))
# print(add(b=2, a=1))


## Sequence Unpacking and Packing ####################
# a = 10
# b = 20

# # a, b = 10, 20

# lst = [10, 20]

# # a, b = lst[0], lst[1]
# a, b = lst                  # Unpacking

# lst = [1, 2, 3, 4]
# # a, b, c = lst # <-- ERROR: 

# lst = [1, 2, [1, 2, 3]]
# a, b, c = lst


# lst = [1, 2, 3]

# print(f"{a=}, {b=}, {c=}")

# def add(a, b):
#     print(f"{a=}, {b=}")
#     return a+b

# for _ in range(5):
#     print(add(1, 2))

# lst = [1, 2, 3]

# a, _, c = lst
# print(f"{a=}, {c=}")

# lst = [1, 2 ,3, 4, 5]
# a, *b, c = lst          # First unpack lst; Pack 2, 3, 4 in to b as a collection (list, as this is local scope)
# a, *_, c = lst
# print(f"{a=}, {b=}, {c=}")



# def add(*nums):     # Packing; Variable arg list
#     print(f"{nums=}")
#     sum = 0
#     for val in nums:
#         sum += val
#     return sum

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))

# lst = [1, 2, 3, 4]
# print(add(*lst))        # Unpacking
# print(add(*lst))


# def PrintEmp(director, tech_lead, **others):    # Keyworded arg list
#     print(others)
#     print("director=", director, "tech_lead=", tech_lead)
#     for pos, name in others.items():
#         print(pos, "=", name)

# PrintEmp("Abhijeet", "Pravin")
# PrintEmp("Abhijeet", "Pravin", sales="Manish")

## Universal

# def add1(a, b):
#     return a+b

# def add2(a, b, c):
#     return a+b+c

# def add3(*, a, b, c):
#     return a+b+c


# def Method(*varArgs, **kwArgs):
#     print(f"\n{varArgs=}\n{kwArgs=}")
#     return add3(*varArgs, **kwArgs)


# #region
# # Method()
# # Method(1, 2, 3)
# # Method(a=1, b=2, c=3)
# # Method(1, 2, 3, a=1, b=2, c=3)
# # Method(1, 2, a=1, b=2, c=3, 3)
# #endregion

# print(Method(a=1, b=2, c=3))

#endregion

#region Special arguments

def Method(a, b, /, c, d, *, e, f):
    pass

Method(1, 2, 3, d=4, e=5, f=6)
Method()



#endregion
