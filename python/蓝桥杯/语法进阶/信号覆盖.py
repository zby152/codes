(W, H, n, R) = map(int, input().split())

towns = []
for _ in range(n):
    temp = list(map(int, input().split()))
    towns.append(temp)

count = 0

for i in range(W + 1):
    for j in range(H + 1):
        flag = 1
        for c in towns:
            if flag == 0:
                break
            dis = (abs(i - c[0]) ** 2) + (abs(j - c[1]) ** 2)
            if dis <= R ** 2:
                count += 1
                flag = 0

print(count)
