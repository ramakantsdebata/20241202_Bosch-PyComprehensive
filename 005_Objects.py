# a = "Test"
# b = "T"
# b += "est"

# if a == b:
#     print("Same")
# else:
#     print("Distinct")

# print(id(a), id(b), sep='\n')

# print(a is b)

# print(type(a is b))

# Value  --> a
# Type --> type(a)
# Identity --> id(a)


a = 10
b = 10

print(a, b, sep="\n")
print(id(a), id(b), sep="\n")


b = 20
print(a, b, sep="\n")
print(id(a), id(b), sep="\n")

a = 30
print(a, b, sep="\n")
print(id(a), id(b), sep="\n")

