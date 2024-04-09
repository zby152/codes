N = int(input())

P = list(map(int, input().split()))

count = 0

for i in range(N):
    if P[i] != i + 1:
        temp = P.index(i + 1)
        P[i], P[temp] = P[temp], P[i]
        count += 1

print(count)
