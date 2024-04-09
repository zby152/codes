Z = 1000
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
M = [[0]*Z for _ in range(Z)]
A = [0] * (Z * Z)
T = list(range(Z * Z))

def P(i, j):
    return i * m + j

def F(n):
    if T[n] != n:
        T[n] = F(T[n])
    return T[n]

n, m = map(int, input().split())
for i in range(n):
    M[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        x, y = i, j
        for dx, dy in D:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and M[x][y] > M[nx][ny]:
                x, y = nx, ny
        T[P(i, j)] = P(x, y)

for i in range(n):
    for j in range(m):
        A[F(P(i, j))] += 1

for i in range(n):
    for j in range(m):
        print(A[P(i, j)], end='\n' if j == m - 1 else ' ')
"""
0 0 0 0 6 0
0 7 0 0 0 0
0 0 0 0 0 4
0 0 7 0 0 0


"""