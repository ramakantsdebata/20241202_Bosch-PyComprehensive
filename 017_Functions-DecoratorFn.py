# def Greet():
#     print("Hi there!!")

# def SayHello():
#     print("Hello")

# def Logger(fn):
#     def Wrapper():
#         print("Calling", fn.__name__)
#         fn()
#         print("Returned from", fn.__name__)
#     return Wrapper

# Greet = Logger(Greet)
# SayHello = Logger(SayHello)

# #####################################################

# Greet()
# print("-"*20)
# SayHello()

# # Wrapper()



####################################################################
####################################################################


def Logger(fn):
    def Wrapper(*vArgs, **kwArgs):
        print("Calling", fn.__name__)
        res = fn(*vArgs, **kwArgs)
        print("Returned from", fn.__name__)
        return res
    Wrapper.__doc__ = fn.__doc__
    return Wrapper

@Logger
def Greet():
    """Greets the user"""
    print("Hi there!!")

# Greet = Logger(Greet)

@Logger
def SayHello():
    """Says Hello to the user"""
    print("Hello")

# SayHello = Logger(SayHello)

@Logger
def add(a, b):
    return a+b

#####################################################

Greet()
print("-"*20)
SayHello()

print(Greet.__doc__)
print(SayHello.__doc__)

# Wrapper()

print(add(1, 2))
