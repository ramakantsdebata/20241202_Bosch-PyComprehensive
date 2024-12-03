# Strings
# s1 = 'They said, "Look out"'
# s2 = "The horse' saddle unbuckled"

# print(s1)
# print(s2)


# s3 = """This is a
# multiline
# string"""

# print(s3)


# s4 = "First""Second"

# # a.b       Bash
# # ab        Python
# print(s4)


#################################

# path = r"C:\Users\temp\newfile.txt"
# print(path)

################################
## Format Strings

# training = "Python"
# days = 12

# s1 = "This is a training for %s over %d days."
# fnl = s1%(training, days)

# print(fnl)

# print("This is a training for %s over %d days." % (training, days))
# print("This is a training for {} over {} days.".format(training, days))
# print(f"This is a training for {training} over {days} days.")

# a = 10
# b = 20
# print(f"a={a}, b={b}")
# print(f"{a=}, {b=}")


###################################################
## Slicing

training = "Python"
days = 12

s1 = f"This is a training for {training} over {days} days."

print(s1)

print(s1[5:])
print(s1[5:15])
print(s1[:15])
print(s1[::2])
print(s1[::-1])
print(s1[-1:])

s2 = "0123456789"
print(s2[3:7])
print(s2[6:2:-1])
print(">>", s2[8:2])
print(s2[8:], s2[:2], sep="")

# Replacing character in a string
# s2[3] = 0

print(type(s2))

a = 10
print(a)
print(str(a))
print(a.__str__())
print(a.__repr__())
# print(len(s2))
# print(s2.__len__())

class Test:
    pass

obj = Test()
print(type(obj))
print(obj)  # obj  --> str(obj) -->  obj.__str__()  --> obj.__repr__()
print(obj.__repr__())
print(repr(obj))


# Implementations and overloads to be seen under the section of classes
