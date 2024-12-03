## Set - Mutable collection of keys
st1 = {}    # <-- Creates a dictionary
st2 = set()

print(type(st2))
st2.add(1)
lst1 = [1, 2, 3, 4, 5]
st2.update(lst1)
print(type(st2), st2)

# lst2 = [1, 2, 3, [1, 2, 3]]
# st2.update(lst2)
# print(st2)

# st2.add([1, 2, 3])

st2.add('a')
st2.add('String')
print(st2)


# Hash - One way transformation of data 
# Requires that the source data never changes, as the hash generated will then have to change again

a = 10
print(hash(a))

s1 = "String"
print(hash(s1))

# lst1 = [1, 2, 3, 4]
# print(hash(lst1))

st3 = {1, 2, 3, 4}# , {1, 2}}
print(type(st3), st3)

st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6}
st3 = {7, 8}

print(st1.union(st2))
# print(st1 + st2)  # <-- ERROR
print(st1 | st2)
print(st1 & st2)    # Intersection
print(st1.isdisjoint(st3))
print(st1 & st3 == set())

st4 = {3, 4}
print(st4.issubset(st1))
print(st4 < st1)

st1.remove(3)
st1.discard(5)
print("All done")

print(st1.pop())


st1 = set()
st1.add(70)
st1.add(23)
st1.add(47)
st1.add(89)
st1.add(56)
st1.add(72)
st1.add(10)

print(st1)
print(st1.pop())
print(st1.pop())
print(st1.pop())
print(st1.pop())


fs1 = frozenset(st1)
print(type(fs1), fs1, hash(fs1))

st1.add(fs1)
print(st1)
