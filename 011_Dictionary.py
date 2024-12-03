# Dictionary - Mutable collection of key-value pairs

dt1 = dict()
dt2 = dict(a ="One", b="Two")
dt3 = {"1":"One", "2":"Two"}

print(f"{dt1=}")
print(f"{dt2=}")
print(f"{dt3=}")

lst = ['a', 'b', '1', '2']
dt4 = dict.fromkeys(lst)
print(f"{dt4=}")

lst2 = list(dt3)

print(f"{lst2}")

print(len(dt4))

print(dt3["1"])
dt3["3"] = "Three"
print(dt3)


# print(dt3['4'])

if '4' in dt3:
    print(dt3['4'])
else:
    print("Key not found")

print(dt3.get('4'))


for item in dt3:
    print(item)

for item in dt3.keys():
    print(item)

for item in dt3.values():
    print(item)

for key, value in dt3.items():
    print(key, "-->", value)

print(dt3.pop("3"))
print(dt3.popitem())
