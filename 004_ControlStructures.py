# if <cond>:
#     # Statements
# elif <cond2>:
#     # Statements
# else:
#     # Statements

# from random import randint


# userCh = input("Enter your choice [1: Rock, 2: Scissors, 3: Paper]: ")
# genCh = randint(1, 3)
# print(userCh, genCh)


# # Not my cup of tea

# x = 5
# if x < 10:
#     pass
# else:
#     print(x)


## Loops - for, while

# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(i, i**2, sep='->', end=' || ')
# print()

# for i in range(11):
#     print("i=", i)


# lst = [1, 2 , 3, 4, 5]

# data = 5
# for val in lst:
#     if val == data:
#         print("Found it")
#         break
# else:
#     print("Not found!")

# print("All Done")


## while

# lst = [1, 2 , 3, 4, 5]

# data = 7
# i = 0
# while i < len(lst):
#     if data == lst[i]:
#         print("Found it")
#         break
#     i += 1
# else:
#     print("Not Found")
    
# i = 10
# while i > 0:
# # while i != 0:
#     print(i)
#     i -= 1


## Match Case
ch = int(input("Enter a number: "))
match ch:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")

        
    
        