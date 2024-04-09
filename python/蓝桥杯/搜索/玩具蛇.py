# 深度优先搜索

direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0
invalide = [[0 for _ in range(4)] for _ in range(4)]


def is_right(x, y):
    if x >= 0 and y >= 0 and x < 4 and y < 4:
        if invalide[x][y] == 0:
            return True
    return False


def DFS(k, x, y):
    global count
    if k == 16:
        count += 1
    else:
        for i in range(4):
            n_x = x + direc[i][0]
            n_y = y + direc[i][1]
            if is_right(n_x, n_y):
                invalide[n_x][n_y] = 1
                DFS(k + 1, n_x, n_y)
                invalide[n_x][n_y] = 0


for i in range(4):
    for j in range(4):
        invalide[i][j] = 1
        DFS(1, i, j)
        invalide[i][j] = 0

print(count)
