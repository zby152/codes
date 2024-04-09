a, b, c = map(int, input().split())
for x in range(0, a):
    if (a - x) ^ (b + x) == c:
        print(x)
        break
