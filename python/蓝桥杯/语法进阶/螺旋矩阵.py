n = 0
m = 0
direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def in_map(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True


(n, m) = map(int, input().split())
(r, c) = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]

di = 0
x = 0
y = 0

for i in range(1, n * m + 1):
    maps[x][y] = i
    n_x = x + direc[di][0]
    n_y = y + direc[di][1]

    if not in_map(n_x, n_y) or maps[n_x][n_y] != 0:
        di = (di + 1) % 4
        n_x = x + direc[di][0]
        n_y = y + direc[di][1]

    x = n_x
    y = n_y

print(maps[r - 1][c - 1])
