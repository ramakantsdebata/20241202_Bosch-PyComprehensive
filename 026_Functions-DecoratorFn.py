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
    def Wrapper():
        print("Calling", fn.__name__)
        fn()
        print("Returned from", fn.__name__)
    return Wrapper

@Logger
def Greet():
    print("Hi there!!")

# Greet = Logger(Greet)

@Logger
def SayHello():
    print("Hello")

# SayHello = Logger(SayHello)

#####################################################

Greet()
print("-"*20)
SayHello()

# Wrapper()