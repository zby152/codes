# 动态规划，01背包问题
import sys

# 重新定义标准输入流为更快的文件对象
input = sys.stdin.readline

n = int(input())
box = []
cap = 0
for _ in range(n):
    w, v = map(int, input().split())
    box.append([w, v, w + v])
    cap += w

box = sorted(box, key=lambda x: x[2])

dp = [0 for i in range(cap + 1)]

for i in range(n):
    w, v = box[i][0], box[i][1]
    for j in range(cap, w - 1, -1):
        if j - w <= v:
            dp[j] = max(dp[j], dp[j - w] + v)

dp.sort()

print(dp[-1])
