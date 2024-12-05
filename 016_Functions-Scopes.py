# LEGB - Local, External, Global, Builtins

# def Outer():
#     # global s1
#     print(f"{locals()=}")

#     s1 = "Outer String"

#     print(f"{locals()=}")

#     def Inner():
#         # nonlocal s1
#         s1 = "Inner String"
#         print(f"Inner --> {s1}")

#     Inner()
#     print(f"Outer --> {s1}")
#     print(f"{locals()=}")
#     print(f"{globals()=}")
#     globals()['s1'] = "Modified String"

# s1 = "Global String"

# Outer()

# print(f"Global --> {s1}")


#######################################################

# def Outer():
#     s1 = "Outer String"

#     def Inner():
#         s1 = "Inner String"
#         print(f"Inner --> {s1}")

#     print(f"Outer --> {s1}")
#     return Inner

# # fn = Outer()
# # fn()

# Outer()()

##############################################

def PowerOf(exp):
    def RaisedTo(num):
        print(num**exp)     # 'exp' is captured in the context of 'RaisedTo()'; This is called a 'Closure'.
    return RaisedTo


# print(PowerOf(2)(4))
# print(PowerOf(3)(4))

PowerOf(2)(4)
PowerOf(3)(4)

Square = PowerOf(2)
Square(3)

Cube = PowerOf(3)
Cube(3)


Square(3)
Cube(3)