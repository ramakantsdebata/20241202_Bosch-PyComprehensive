#region Manually enabling method overloading via proxy function 
# def add(a, b):
#     return a+b

# print(f"{type(add)=}")
# print(f"{add=}")
# # print(add(1, 2))

# add_old = add
# def add(a, b, c):
#     return a+b+c

# print(f"{type(add)=}")
# print(f"{add=}")

# # print(add(1, 2))
# # print(add(1, 2, 3))


# # extern "C"
# # void add(int a, int b);             --> _add_int_int
# # void add(int a, int b, int c);      --> _add_int_int_int

# # int res = add(1, 2)

# # float res = add(1, 2)
# # add(1, 2)

# # printf("")

# def add1(a, b):
#     return a+b

# def add2(a, b, c):
#     return a+b+c

# def add3(a, b, c, d):
#     return a+b+c+d

# def add(*vArg):
#     argCount = len(vArg)

#     if argCount < 2 or argCount > 4:
#         raise Exception("Invalid no. of arguments")
    
#     match argCount:
#         case 2:
#             return add1(*vArg)
#         case 3:
#             return add2(*vArg)
#         case 4:
#             return add3(*vArg)


# # print(f"{add(1)=}")
# print(f"{add(1, 2)=}")
# print(f"{add(1, 2, 3)=}")
# print(f"{add(1, 2, 3, 4)=}")
#endregion

#region virtual env identification
# import sys

# print(f"{sys.base_prefix=}")
# print(f"{sys.prefix=}")
#endregion

#region Using the module multipledispatch

from multipledispatch import dispatch

@dispatch(int, int)
def add(a:int, b:int)->int:
    print("Using the add(int, int)->int")
    return a+b

@dispatch(str, str)
def add(a:str, b:str)->str:
    print("Using the add(str, str)->str")
    return a+b

@dispatch(int, int, int)
def add(a, b, c):
    print("Using the add(int, int, int)->int")
    return a+b+c

print(add(1, 2))
print(add(1, 2, 3))
print(add("Test", "String"))

#endregion 
