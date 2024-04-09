#不能用深搜，会超时
N, M = map(int, input().split())

e = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

ans = 0

for i in range(1,N+1):
    for j in e[i]:
        for k in e[j]:
            if k!=i:
                ans+=len(e[k])-1

print(ans)
