direc = [[0, 1], [1, -1], [-1, 0]]
n = 0


def in_map(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    else:
        return False


n = int(input())

result = [[0 for _ in range(n)] for _ in range(n)]

index = 1
location = [0, 0]
di = 0

while index <= (n + 1) * n / 2:
    result[location[0]][location[1]] = index
    index += 1
    n_x = location[0] + direc[di][0]
    n_y = location[1] + direc[di][1]
    if not in_map(n_x, n_y) or result[n_x][n_y] != 0:
        di = (di + 1) % 3
        n_x = location[0] + direc[di][0]
        n_y = location[1] + direc[di][1]
    location = [n_x, n_y]

for i in range(n):
    for j in range(n - i):
        print(result[i][j], end=' ')
    print()
