n = int(input())

X = list(map(int, input().split()))

first = X[0]
count = 1

if first > 0:
    for x in X:
        if x < 0 and abs(x) > abs(first):
            count += 1
    if count > 1:
        for x in X:
            if x > 0 and abs(x) < abs(first):
                count += 1

else:
    for x in X:
        if x > 0 and abs(x) < abs(first):
            count += 1
    if count > 1:
        for x in X:
            if x < 0 and abs(x) > abs(first):
                count += 1

print(count)
