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

# res = re.findall(r"(.+?)", string1)
# print(res)

# res = re.findall(r"[(.+?)]", string1)
# print(res)

# res = re.findall(r"[a-zA-Z1-5_]")

# res = re.findall(r"[ \n\t\v\f\c]")      # All the whitespace characters



## Curly Braces {} - Quantifier

# res = re.findall(r"\d{2,4}", string1)
# print(res)


# res = re.findall(r"\w{2,4}", string1)
# print(res)


# res = re.findall(r"\w{3,}", string1)
# print(res)

# res = re.findall(r"\w{2,6}", string1)
# print(res)

# res = re.findall(r"\w{2,6}?", string1)
# print(res)


## Pipe  - Combination of conditions; First one to match returns result

# # A|B|C -Whichever condition matches successfully; If more than one conditions match, sequence of conditions matters
# res = re.search(r"\d{2}|\d{3}|\w{6}", string1)
# print(res)





## Sepcial Sequences ##########################################################
# \A (Beginning of string) & \Z (End of string)
# string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe\n including the \nFTSE, fell\n by 11.48% - \nthe worst day since it launched in 1998.\nThe panic selling \nprompted by \nthe coronavirus has wiped £2.7tn off the value of STOXX 600 shares since\n its all-time peak on 19 February"
# res = re.findall(r"\AThe", string1, re.M|re.I)
# print(len(res), res)

# res  = re.findall(r"\w+\Z", string1, re.M)
# print(res)


# \b (word boundary) & \B (Non-boundary)
string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

res = re.search(r"\b\w{2}\b", string1) 
print(res)

res = re.search(r"\Bcross\B", string1)
print(res)


# \d (digit) & \D (non-digit)

res = re.findall(r"\B\d{2}\B", string1)
print(res)


# \s (whitespaces) & \S (Non-whitespaces)

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe\n including the \nFTSE, fell\n by 11.48% - \nthe worst day since it launched in 1998.\nThe panic selling \nprompted by \nthe coronavirus has wiped £2.7tn off the value of STOXX 600 shares since\n its all-time peak on 19 February"
res = re.findall(r"\s", string1)
print(res)


# \w (alphanumeric and _)  & \W (opposite of \w)
