import math

HS = 11625907.5798
n = 23333333


def calculate(num):
    p0 = num / n
    p1 = 1 - p0
    left = (1 - p0) ** 2 * math.log2(p1)
    right = p0 ** 2 * math.log2(p0)
    summ = -left - right
    result = HS / n - summ

    return abs(result)


min_p = 1
min_n0 = 1
for n0 in range(1, n // 2):
    temp = calculate(n0)
    if temp < min_p:
        min_p = temp
        min_n0 = n0

print(min_n0)
