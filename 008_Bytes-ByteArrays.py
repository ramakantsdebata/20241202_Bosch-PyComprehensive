# Bytes - Immutables
# ByteArray - Mutable

# a = 10
# b = bytes(10)
# print(type(b), b)

# data = b"TestString"
# print(type(data), data)
# strDecoded = str(data)          # This only strigifies the data obj, does NOT really convert it to a str type
# print(type(strDecoded), strDecoded)

# strDecoded = data.decode()
# print(type(strDecoded), strDecoded)

#################################################

s2 = "This is a string"
print(type(s2), s2)
byteData = s2.encode(encoding="utf-8")

print(type(byteData), byteData)

s3 = byteData.decode()
print(type(s3), s3)

