N = int(input())


def ou(a):
    return int(a / 2)


def ji(a):
    return a * 3 + 1


max_a = 0
for i in range(2, N + 1):
    a = i
    while a != 1:
        if a % 2 == 0:
            a = ou(a)
        else:
            a = ji(a)
        if a > max_a:
            max_a = a
        if a < i:
            break
print(max_a)
