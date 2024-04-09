x = input()
result = []

for i in x:
    temp = ord(i)
    if temp <= 119:
        temp += 3
        result.append(chr(temp))
    else:
        temp -= 23
        result.append(chr(temp))

print("".join(result))
