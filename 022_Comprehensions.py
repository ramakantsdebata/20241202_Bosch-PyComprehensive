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
