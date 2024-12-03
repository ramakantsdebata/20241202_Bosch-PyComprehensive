# Bytes - Immutables
# ByteArray - Mutable

a = 10
b = bytes(10)
print(type(b), b)

data = b"TestString"
print(type(data), data)
strDecoded = str(data)          # This only strigifies the data obj, does NOT really convert it to a str type
print(type(strDecoded), strDecoded)

strDecoded = data.decode()
print(type(strDecoded), strDecoded)
