yuan = ["a", "e", "i", "o", "u"]

string = input()

y = 0
f = 0
for ch in string:
    if ch in yuan:
        y += 1
    else:
        f += 1

print(y)
print(f)
