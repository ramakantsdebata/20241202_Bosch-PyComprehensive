# def CallCounter(fn):
#     globals()[fn.__name__ + '_counter'] = 0
#     def Wrapper():
#         globals()[fn.__name__ + '_counter'] += 1
#         fn()
#     return Wrapper

def CallCounter(fn):
    def wrapper():
        if globals()[fn.__name__ + '_counter']:
            globals()[fn.__name__ + '_counter'] += 1
        else:
            globals()[fn.__name__ + '_counter'] = 1
        fn()
    return wrapper


@CallCounter
def Greet():
    print("Hi there!!")

@CallCounter
def SayHello():
    print("Hello")

@CallCounter
def SayHi():
    print("Hi")

# globals()
# fn.__name__


#####################################################

Greet()
Greet()
Greet()
Greet()
Greet()
Greet()
print("-"*20)
SayHello()
SayHello()
SayHello()
SayHello()


print(Greet_counter)
print(SayHello_counter)
print(SayHi_counter)
