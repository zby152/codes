days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(y):
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0


def daysOfMonth(y, m):
    if m == 2 and is_leap(y):
        return 29
    return days[m]


def check(x, y, z):
    s1 = 0
    while x:
        s1 += x % 10
        x //= 10
    s2 = 0
    while y or z:
        s2 += y % 10
        s2 += z % 10
        y //= 10
        z //= 10
    return s1 == s2


res = 0
for i in range(1900, 10000):
    for j in range(1, 13):
        for k in range(1, daysOfMonth(i, j) + 1):
            res += check(i, j, k)
print(res)
