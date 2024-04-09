# 全排列方法

from itertools import permutations

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def invalid(l):
    if l[0] + l[1] + l[2] == 15 and l[3] + l[4] + l[5] == 15 and l[6] + l[7] + l[8] == 15 and l[0] + l[3] + l[
        6] == 15 and l[1] + l[4] + l[7] == 15 and l[2] + l[5] + l[8] == 15 and l[0] + l[4] + l[8] == 15 and l[2] + l[
        4] + l[6] == 15:
        return True
    else:
        return False


maps = []
for _ in range(3):
    maps.extend(map(int, input().split()))

count = 0
for p in permutations(s):
    flag = 1
    for i in range(9):
        if maps[i] != 0 and maps[i] != p[i]:
            flag = 0
            break
    if flag == 1 and invalid(p):
        count += 1
        res = p

if count == 1:
    for i in range(3):
        for j in range(3):
            print(res[i * 3 + j], end=" ")
        print()

else:
    print("Too Many")
