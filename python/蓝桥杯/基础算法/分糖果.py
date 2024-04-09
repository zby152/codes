# 去掉重复元素的方法

N = int(input())
tang = list(map(int, input().split()))
count = 0
flag = 0

while flag == 0:
    temp = []
    for i in range(N):
        temp.append(int(tang[i] / 2 + tang[(i + 1) % N] / 2))
        if temp[-1] % 2 == 1:
            count += 1
            temp[-1] += 1
        temp2 = list(set(temp))
    tang = temp.copy()
    if len(temp2) == 1:
        flag = 1

print(count)
