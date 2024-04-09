# 差分和前缀和问题

n, m = map(int, input().split())
d = [[0]*(n+2) for _ in range(n+2)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    d[x1][y1] += 1
    d[x1][y2+1] -= 1
    d[x2+1][y1] -= 1
    d[x2+1][y2+1] += 1

for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = d[i][j] + d[i-1][j] + d[i][j-1] - d[i-1][j-1]
        if d[i][j]&1:
            print("1", end="")
        else:
            print("0", end="")
    print()