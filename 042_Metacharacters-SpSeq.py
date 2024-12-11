# Metacharacters and Special Sequences

# . - Mathces anything , except for the newline. With a flag of re.DOTALL, it mathces the newline as well.

# ^ - Matches the beginning a of a line, as opposed to string

import re
string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# res = re.search(r"^\w{3}", string1)
# if res:
#     print(res)
# else:
#     print("Pattern not found")


# # res = re.search(r"(\d{2}\s\w+).$", string1)
# res = re.search(r"\w+\W$", string1)
# if res:
#     print(res)
# else:
#     print("Pattern not found")




# ## * - 0 or more occurance of preceeding pattern

# res = re.findall(r"\w*", string1)
# print(res)


# res = re.findall(r"E\w*", string1)
# print(res)


# ## + - 1 or more occurances of preceeding pattern

# res = re.findall(r"\w+", string1)
# print(res)


# res = re.findall(r"E\w+", string1)
# print(res)


# ? - 0 or 1 occurances of the preceeding pattern

# res = re.findall(r"\d\d\d*", string1)
# print(res)
# res = re.findall(r"\d\d+", string1)
# print(res)


# res = re.findall(r"\d\d\d?", string1)       # Non-greedy quantifier
# print(res)



# res = re.findall(r"\d\d\d*?", string1)
# print(res)
# res = re.findall(r"\d\d+?", string1)
# print(res)
# res = re.findall(r"\d\d\d*", string1)
# print(res)
# res = re.findall(r"\d\d\d??", string1)
# print(res)


# \ - can be used in one of two roles:
#   1. Special Sequences - \w \W \d \D
#   2. Escape the special meaning of the metacharacters  \.   \d\d\d\d\? 

# string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February?"

# res = re.search(r""".+\s  # IGNORE: Few characters followed by a whitespace
#                 (.+ex)    # >> any word ending with 'ex'
#                 .+        # IGNORE: Intermediate characters to ignore
#                 (\d\d.+)  # >> Date to pickup
#                 \.         # <<--- Suppressing the metacharacter might lead to unexpected behaviour here.
#                 """, string1, re.X)      # re.VERBOSE)
# print(res.groups())


## [] - Character set

# strPattern = r"[abcde]"
# strPattern = r"[a-e]"
# res = re.findall(strPattern, string1)
# print(len(res), res)


# strPattern = r"[^abcde]"
# strPattern = r"[^a-e]"
# res = re.findall(strPattern, string1)
# print(len(res), res)


# # 1800-1819 1900-1919
# string2 = "This revolution started in 1801, continued through 1811 till 1819. Documented in 1845"
# res = re.findall(r"1[8-9][0-1][0-9]", string2)
# print(res)

res = re.findall(r"(.+?)", string1)
print(res)

res = re.findall(r"[(.+?)]", string1)
print(res)

res = re.findall(r"[a-zA-Z1-5_]")

res = re.findall(r"[ \n\t\v\f\c]")      # All the whitespace characters
