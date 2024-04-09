yuan = ["a", "e", "i", "o", "u"]

string = input()
last = 1
result = 0

for ch in string:
    if ch in yuan:
        if last == 1:
            continue
        else:
            result += 1
            last = 1
    else:
        if last == 1:
            result += 1
            last = 0
        else:
            continue

if result == 4:
    print("yes")

else:
    print("no")
