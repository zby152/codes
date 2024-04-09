# 动态规划问题和二叉树结合
MOD = 1000000009
N = 100001
fact = [0 for _ in range(N)]
infact = [0 for _ in range(N)]


def qpow(b, e):
    """快速幂算法"""
    result = 1
    while e != 0:
        if (e & 1) == 1:
            # ei = 1, then mul
            result = (result * b) % MOD
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b * b) % MOD
    return result


def comb(n, m):
    return fact[n] * infact[m] % MOD * infact[n - m] % MOD


if __name__ == "__main__":

    n = int(input())

    # 预处理阶乘
    fact[0] = infact[0] = 1
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
        infact[i] = infact[i - 1] * qpow(i, MOD - 2) % MOD

    dp = [0 for _ in range(n + 1)]

    dp[1] = dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        d = 20  # 二叉树最高层数
        left = 0
        right = 0
        # 找到二叉树的层数d
        while i <= qpow(2,d+1) - 1:
            d -= 1

        x1=qpow(2,d+1)
        x2=qpow(2,d)

        full = x1 - 1 # 完全二叉树节点个数
        last = i - full
        if last >= x2:
            left = x1 - 1
            right = i - 1 - left
        else:
            right = x2 - 1
            left = i - 1 - right

        dp[i] = (comb(i - 1, left) % MOD * ((dp[left] % MOD * (dp[right] % MOD)) % MOD)) % MOD

    print(dp[n])
