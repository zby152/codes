(m, n) = map(int, input().split())

h = n
w = h + m - 1
result = [["." for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(m):
        result[i][i + j] = "*"

for i in range(h):
    for j in range(m):
        result[i][w - j - i - 1] = "*"

for i in range(h):
    for j in range(w):
        print(result[i][j], end='')
    if i < h - 1:
        print()
