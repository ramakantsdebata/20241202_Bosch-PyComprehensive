# (?{extn}{expr})

import re

string1 = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


## ?:   Comment a group
# res = re.search(r".+\s(.+ex).+(\b[A-Z]{4}\b).+(\d\d.+).", string1)
# print(res.groups())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))



# res = re.search(r".+\s(?:.+ex).+(?:\b[A-Z]{4}\b).+(\d\d.+).", string1)
# print(res.groups())
# print(res.group(1))
# # print(res.group(2))


## ?P<name>
# res = re.search(r".+\s(?P<wordex>.+ex).+(?P<block_word>\b[A-Z]{4}\b).+(?P<date>\d\d.+).", string1)
# print(res.groups())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))

# print(res.group("wordex"))
# print(res.group("block_word"))
# print(res.group("date"))

# print(res.groupdict())
# print(res.groupdict()["wordex"])
# print(res.groupdict()["block_word"])
# print(res.groupdict()["date"])


# string2 = "Paris in the the time of spring"
# res = re.findall(r"\b(?P<word>\w+)\s(?P=word)\b", string2)
# print(res)


## Positive LookAhead Notation
# "{trgt-pattern}(?=chk-pattern)"

res = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string1)
print(res)


## Negative LookAhead Notation
# "{trgt-pattern}(?!chk-pattern)"

res = re.findall(r"\d(?![6-9]|\D)", string1)
print(res)

## Positive LookBehind Notation
# "(?<=chk-pattern){trgt-pattern}"

res = re.findall(r"(?<=\s)\d+", string1)
print(res)


## Negative LookBehind Notation
# "(?<!chk-pattern){trgt-pattern}"

res = re.findall(r"(?<!\s)\d+", string1)
print(res)
