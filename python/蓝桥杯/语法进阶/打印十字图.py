direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n = int(input())

col = 1 + 4 * n
N = 5 + 4 * n

result = [["." for _ in range(N)] for _ in range(N)]

# 横线
for x in range(n + 1):

    y = 2 * x
    for i in range(2 + y, N - 2 - 2 * x):
        j = y
        result[i][j] = "$"
    for j in range(2 + y, N - 2 - 2 * x):
        i = y
        result[i][j] = "$"
    for i in range(2 + y, N - 2 - 2 * x):
        j = N - 1 - y
        result[i][j] = "$"
    for j in range(2 + y, N - 2 - 2 * x):
        i = N - 1 - y
        result[i][j] = "$"

# 三角
for i in range(2, N):
    j = i
    if i % 2 == 0 and i <= N // 2:
        result[i][j] = "$"
        result[i - 1][j] = "$"
        result[i][j - 1] = "$"
for i in range(2, N - 2):
    j = i
    if i % 2 == 0 and i >= N // 2:
        result[i][j] = "$"
        result[i][j + 1] = "$"
        result[i + 1][j] = "$"
for i in range(2, N):
    j = N - i - 1
    if i % 2 == 0 and i <= N // 2:
        result[i][j] = "$"
        result[i - 1][j] = "$"
        result[i][j + 1] = "$"
for i in range(2, N - 2):
    j = N - i - 1
    if i % 2 == 0 and i >= N // 2:
        result[i][j] = "$"
        result[i][j - 1] = "$"
        result[i + 1][j] = "$"

for i in range(N):
    for j in range(N):
        print(result[i][j], end='')
    if i < N:
        print()
