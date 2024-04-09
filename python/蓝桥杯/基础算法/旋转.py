(n, m) = map(int, input().split())
start = []
for _ in range(n):
    temp = list(map(int, input().split()))
    start.append(temp)
i = 0
j = 0
end = [[0 for _ in range(n)] for _ in range(m)]
for b in range(n - 1, -1, -1):
    for a in range(m):
        end[a][b] = start[i][j]
        j = j + 1
        if j == m:
            j = 0
            i += 1
for i in range(m):
    for j in range(n):
        print(end[i][j], end=" ")
    print()
