#region Generator basics
# def MyGenerator():
#     yield 1
#     yield 2
#     yield 3

# def Main():
#     it = MyGenerator()
#     print(type(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))

# def Main2():
#     for val in MyGenerator():
#         print(val)


# Main()


# Iterables implement
#     __iter__()

# Iterators NotImplemented
#     __iter__()
#     __next__()

# All iterators can act as iterables
# Calling iter() on an iterator will return itself

# lst = [1, 2, 3, 4]
# it = iter(lst)          # Returns an iterator for the list

# it2 = iter(it)
# # next(it2)

# print(type(it))
# print(type(it2))

#endregion

def FibGen(n):
    """Generator function for Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        if a < n:
            yield a
        else:
            break
        a, b = b, a+b

def Main():
    it = FibGen(100)

    for val in it:
        print(val, end=", ")

Main()
