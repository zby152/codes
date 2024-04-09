# 二叉树找规律类型

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    floor_number = []
    number = 0
    f = 1
    flag = 0
    if n == 1:
        print(1)
        continue
    for floor in range(1, n + 1):
        temp = m ** (floor - 1)
        number += temp

        if k <= number and k >= number - temp:
            if flag == 0:
                f = floor
            if k == number - temp or k == number:
                flag = 1
        if number > n:
            floor_number.append(n - number + temp)
            break
        floor_number.append(temp)
    max_f = len(floor_number)
    ans = 0
    for i in range(len(floor_number) - f):
        ans += m ** i
    a = floor_number[-2] * m  # 最后一行最多有多少节点
    b = (m ** (f - 1))  # 需要分成几份
    c = k - sum(floor_number[:f - 1])  # k在第几份
    front = (a // b) * (c - 1)
    l = sum(floor_number[:-1]) + front + 1
    r = l + (a // b) - 1
    if n >= l and n < r:
        ans += n - l + 1
    if n > r:
        ans += (a // b)
    print(ans)

"""
1
74 5 3
"""
