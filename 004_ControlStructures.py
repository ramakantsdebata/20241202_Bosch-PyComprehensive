# if <cond>:
#     # Statements
# elif <cond2>:
#     # Statements
# else:
#     # Statements

from random import randint


userCh = input("Enter your choice [1: Rock, 2: Scissors, 3: Paper]: ")
genCh = randint(1, 3)
print(userCh, genCh)



