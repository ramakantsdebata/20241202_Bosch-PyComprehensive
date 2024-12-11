import re

path = r"c:\user\newfile.txt"
print(path)


# string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
#     including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
#     The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
#     of STOXX 600 shares since its all-time peak on 19 February."

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# strPattern = r"\d{3}"
# print(f"{type(strPattern)}, {strPattern}")

# rePattern = re.compile(strPattern)
# print(f"{type(rePattern)}, {rePattern}")

# res = re.findall(rePattern, string1)
# print(res)

# res = rePattern.findall(string1)
# print(res)

# res = re.findall(strPattern, string1)
# print(res)


## Search - Finds the first occurance; returns match obj if pattern matched, else return None
# strPattern = r"\d{5}"

# res = re.search(strPattern, string1)
# print(f"{type(res)}, {res}")
# if res != None:
#     print(res.span())
#     print(res.start(), res.end())
#     print(string1[res.start():res.end()])
# else:
#     print("No match found!")

## Match - The pattern should be starting from the beginning of the string

# res = re.match(r"\w{3}", string1)
# if res != None:
#     print(res)
# else:
#     print("Match not found!")

## Full Match - Like the 'Match' start from the beginning of the string; 
# It has to match the entire string, else fails

# print(len(string1))
# # res = re.fullmatch(r".{297}", string1)
# # res = re.fullmatch(r"\w{297}", string1)
# res = re.fullmatch(r".{298}", string1)
# if res != None:
#     print(res)
# else:
#     print("Match not found!")



## Split -  Can split using patterns
# print(string1.split())
# print((string1.lower()).split("the"))

# res = re.split(r"\s", string1)
# if res != None:
#     print(res)
# else:
#     print("Match not found!")



## Sub/Subn - Substitute substring

# res = re.sub(r"[A-Z]{4}", "****", string1)
# if res != None:
#     print(res)
# else:
#     print("Match not found!")


# res = re.sub(r"[A-Z]{4}", "****", string1, 2)
# if res != None:
#     print(res)
# else:
#     print("Match not found!")


# res = re.subn(r"\w{7}", "**", string1, 10)
# if res != None:
#     print(res[1])
#     print(res[0])
# else:
#     print("Match not found!")


## Groups
res = re.search(r".+\s(.+ex).+(\d\d.+).", string1)
print(res)
print(res.groups())
print(res.group())
print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(1, 2))


print(res.start(1), res.end(1))
print(res.start(2), res.end(2))
print(res.span(1))
print(res.span(2))
