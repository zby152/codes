(n, m) = map(int, input().split())
t = int(input())

maps = [[1 for _ in range(m)] for _ in range(n)]

for _ in range(t):
    (r1, c1, r2, c2) = map(int, input().split())
    for i in range(r1 - 1, r2):
        for j in range(c1 - 1, c2):
            maps[i][j] = 0

count = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            count += 1

print(count)
