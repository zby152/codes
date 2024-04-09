# 经典动态规划题型
str1 = input()
str2 = input()

x1 = []
x2 = []

temp = str1[0]
for i in str1:
    if i.isupper():
        x1.append(temp)
        temp = i
    else:
        temp = temp + i
x1.append(temp)
x1.pop(0)
temp = str2[0]
for i in str2:
    if i.isupper():
        x2.append(temp)
        temp = i
    else:
        temp = temp + i
x2.append(temp)
x2.pop(0)

dp = [[0 for _ in range(len(x2) + 1)] for _ in range(len(x1) + 1)]

for i in range(1, len(x1) + 1):
    for j in range(1, len(x2) + 1):
        if x1[i - 1] == x2[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(x1)][len(x2)])
