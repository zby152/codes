# 联合主键排序
# 平方sqrt速度更快

from math import sqrt


def find(num):
    for a in range(int(sqrt(num)) + 1):
        num2 = num - a ** 2
        for b in range(a, int(sqrt(num2)) + 1):
            num3 = num2 - b ** 2
            for c in range(b, int(sqrt(num3)) + 1):
                num4 = num3 - c ** 2
                d = int(sqrt(num4))
                if d >= c and a ** 2 + b ** 2 + c ** 2 + d ** 2 == num:
                    return a, b, c, d


n = int(input())
(r_a, r_b, r_c, r_d) = find(n)
print(r_a, end=' ')
print(r_b, end=' ')
print(r_c, end=' ')
print(r_d, end='')
