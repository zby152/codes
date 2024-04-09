direc = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
n = 0
m = 0


def in_map(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    else:
        return False


(n, m) = map(int, input().split())

maps = []
for _ in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)

result = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            result[i][j] = 9
        else:
            count = 0
            for di in direc:
                n_x = i + di[0]
                n_y = j + di[1]
                if in_map(n_x, n_y) and maps[n_x][n_y] == 1:
                    count += 1
            result[i][j] = count

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    if i < n - 1:
        print()
