# 简单递归的动态规划问题
s = list(input())

check = ["00", "11", "0?", "?0", "1?", "?1", "??"]
dp = [0 for _ in range(len(s))]

if ''.join(s[:2]) in check:
    dp[1] = 1
for i in range(2, len(s)):
    if "".join(s[i - 1:i + 1]) in check:
        dp[i] = dp[i - 2] + 1
    else:
        dp[i] = dp[i - 1]

print(dp[-1])
