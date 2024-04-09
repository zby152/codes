# 深搜

direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
res = []


def inlaw(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    else:
        return False


def dfs(i, j):
    global l, r, step
    if l == r:
        res.append(step)
    elif l < r:
        for di in range(4):
            n_i = i + direc[di][0]
            n_j = j + direc[di][1]
            if inlaw(n_i, n_j) and vis[n_i][n_j]==0:
                step += 1
                l += maps[n_i][n_j]
                r -= maps[n_i][n_j]
                vis[n_i][n_j] = 1
                dfs(n_i, n_j)
                vis[n_i][n_j] = 0
                step -= 1
                l -= maps[n_i][n_j]
                r += maps[n_i][n_j]


(m, n) = map(int, input().split())
maps = []
for _ in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)

vis = [[0 for _ in range(m)] for _ in range(n)]

l = maps[0][0]
r = 0-maps[0][0]
for i in range(n):
    r += sum(maps[i])
step = 1
vis[0][0] = 1
dfs(0, 0)
if len(res)!=0:
    res=sorted(res)
    print(res[0])
else:
    print(0)
