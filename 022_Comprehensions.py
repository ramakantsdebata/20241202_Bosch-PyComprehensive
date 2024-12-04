fruits = ["apple", "banana", "custurd apple", "dragon", "kiwi", "chiku", "mango"]

bowl = []

for fr in fruits:
    if 'a' in fr:
        bowl.append(fr)

print(bowl)


# Comprehension -  Technique to create a collection from an existing collection

lst = [fr         for fr in fruits         if 'a' in fr]
print(type(lst), lst)

st = {fr         for fr in fruits         if 'a' in fr}
print(type(st), st)

dt = {fr:len(fr)         for fr in fruits         if 'a' in fr}
print(type(dt), dt)

tp = tuple(fr         for fr in fruits         if 'a' in fr)
print(type(tp), tp)


# members = dir(int)
# public_members = []
# for item in members:
#     if item.startswith('_') == False:
#         public_members.append(item)

# This give us the public members; 
# We need to check which ones are functions and only create a collection of public functions

obj = 10

public_members = [item    for item in dir(obj)    if item.startswith("_") == False]
public_functions = [item    for item in dir(obj)    if item.startswith("_") == False and callable(getattr(obj, item)) == True]
print(len(public_members))
print(len(public_functions))

def func1():
    print("Hi")

func2 = 10

print(callable(func1))
print(callable(func2))
print(callable(getattr(int, 'bit_count')))
print(callable(int.bit_count))
