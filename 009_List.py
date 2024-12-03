## List  --> Mutable collection of heterogeneous data

# l1 = []
# l2 = list()

# l3 = [1,2 , 3, 4]
# l4 = list("TestString")


# print(l1, l2, l3, l4, sep="\n")

# l4.append("AString")
# l4.append(1234)

# class Test:
#     pass

# l4.append(Test())

# print(l4)
# #  1, 2, 3, 4

# l4.extend([10, 20, 30, 40])
# print(l4)

# print("AString" in l4)

# l4 = list("String")

# print("\n\n")

# l5 = l3 + l4
# l3 += l4
# print(f"{l5=}, {l3=}\n\n")

# l3 = [1, 2, 3, 4]
# l6 = l3 * 2
# print(f"{l6=}\n")
# print("#"*80)

# print(len(l3))
# print(f"{max(l3)=}")

# print(f"{max(l4)=}")
# print(f"{l3=}, {sum(l3)=}")


# members = dir(list)
# public_members = []
# for item in members:
#     if item.startswith('_') == False:
#         public_members.append(item)

# print(public_members)
# del public_members[2]
# print(public_members)

#########################################################

s1 = "Manish"
s2 = s1
print(id(s1), id(s2), sep="\n")
s1 += "!!"
print(id(s1), id(s2), sep="\n")
print(s1, s2)

#-----------------------------------

l1 = [1, 2, 3, 4]
# l2 = l1
# l2 = list(l1)
l2 = l1[:]
l1.append(5)
print(l1, l2)
