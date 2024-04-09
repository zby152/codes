import collections

direc = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def in_map(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    else:
        return False


(n, m) = map(int, input().split())
maps = []
wait_g = collections.deque()

for i in range(n):
    maps.append(list(input()))
    for j in range(m):
        if maps[i][j] == 'g':
            wait_g.append([i, j, 0])
k = int(input())

for K in range(1, k + 1):
    while wait_g[0][2] == K - 1:
        now_g = wait_g.popleft()
        for d in direc:
            n_x = now_g[0] + d[0]
            n_y = now_g[1] + d[1]
            if in_map(n_x, n_y) and maps[n_x][n_y] == '.':
                maps[n_x][n_y] = 'g'
                wait_g.append([n_x, n_y, K])

for i in range(n):
    for j in range(m):
        print(maps[i][j], end="")
    if i < n - 1:
        print()
