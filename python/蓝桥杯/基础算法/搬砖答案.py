import sys

# 重新定义标准输入流为更快的文件对象
input = sys.stdin.readline

count = int(input().strip())
structs = [[0, 0, 0] for _ in range(count + 1)]
capacity = 0

for i in range(1, count + 1):
    wi, vi = map(int, input().strip().split())
    capacity += wi
    structs[i][0] = wi
    structs[i][1] = vi
    structs[i][2] = wi + vi

structs.sort(key=lambda x: x[2])
dp = [0] * (capacity + 1)

for i in range(1, count + 1):
    wi, vi = structs[i][0], structs[i][1]
    for j in range(capacity, wi - 1, -1):
        if j - wi <= vi:
            dp[j] = max(dp[j - wi] + vi, dp[j])

dp.sort()
print(dp[capacity])