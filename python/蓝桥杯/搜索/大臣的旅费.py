# 动态规划问题
# 注意是双向图
# dp[u]代表的是u已经访问过的前面的节点所能提供的最大的路径
# 所以每一次都需要去考虑最大的长度为两个节点的其他节点能提供的路径加上两个节点之间的
# 每次考虑是否将dp[v]+step这一支作为最大的路径

max_len = 0


def DFS(u):
    global max_len
    for v, step in e[u]:
        if invited[v] == 1:
            continue
        else:
            invited[v] = 1
            DFS(v)
            max_len = max(max_len, dp[u] + dp[v] + step)
            dp[u] = max(dp[u], dp[v] + step)


n = int(input())
dp = [0 for _ in range(n + 1)]
e = [[] for _ in range(n + 1)]
invited = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    (p, q, d) = map(int, input().split())
    e[p].append((q, d))
    e[q].append((p, d))

invited[1] = 1
DFS(1)

sum_ = (11 + (max_len + 10)) * max_len // 2
print(sum_)
