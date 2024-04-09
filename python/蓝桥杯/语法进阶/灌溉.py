import copy

direc = [[-1, 0], [0, -1], [0, 1], [1, 0]]
n = 0
m = 0


def in_map(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    else:
        return False


(n, m) = map(int, input().split())
t = int(input())

maps = [[0 for _ in range(m)] for _ in range(n)]
n_maps = [[[0 for _ in range(m)] for _ in range(n)]]

for _ in range(t):
    (r, c) = map(int, input().split())
    maps[r - 1][c - 1] = 1

k = int(input())

for times in range(k):
    n_maps = copy.deepcopy(maps)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                for di in direc:
                    n_x = i + di[0]
                    n_y = j + di[1]
                    if in_map(n_x, n_y):
                        n_maps[n_x][n_y] = 1
    # print(maps)
    # print(n_maps)
    maps = copy.deepcopy(n_maps)

count = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            count += 1

print(count)
