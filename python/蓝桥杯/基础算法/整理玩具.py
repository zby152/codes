from collections import deque

directions = [[0, 1], [1, 0], ]
n, m = 0, 0


def inlaw(x, y, vis2):
    if x >= 0 and x < n and y >= 0 and y < m:
        if vis2[x][y] == 0:
            return True
    return False


def bfs(num, vis, vis2, boxs):
    if vis[num] == 1:
        return False
    vis[num] = 1
    cnt = 1
    max_col, max_row = 0, 0
    s_x = Q[0][0]
    s_y = Q[0][1]
    while len(Q) > 0:
        x, y = Q.popleft()
        for di in range(2):
            n_x = x + directions[di][0]
            n_y = y + directions[di][1]
            if inlaw(n_x, n_y, vis2) and boxs[n_x][n_y] == num:
                max_row = max(max_row, n_x - s_x)
                max_col = max(max_col, n_y - s_y)
                vis2[n_x][n_y] = 1
                cnt += 1
                Q.append([n_x, n_y])
    if (max_col + 1) * (max_row + 1) == cnt:
        return True
    else:
        return False


def solve():
    global n, m
    Q.clear()
    n, m = map(int, input().split())
    boxs = []
    for _ in range(n):
        temp = list(map(int, list(input())))
        boxs.append(temp)
    vis = [0 for _ in range(10)]
    vis2 = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            number = boxs[i][j]

            if vis2[i][j] == 1:
                continue
            vis2[i][j] = 1

            Q.append([i, j])
            if bfs(number, vis, vis2, boxs):
                continue
            else:
                print("NO")
                return False
    print("YES")


Q = deque()
T = int(input())
for _ in range(T):
    solve()

"""
1
4 4
1122
1122
3344
3344
"""
