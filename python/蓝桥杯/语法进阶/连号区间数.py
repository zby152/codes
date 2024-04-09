N = int(input())
p = list(map(int, input().split()))
# N=4
# p=[3,2,4,1]
result = 0

for i in range(N):
    max_ = p[i]
    min_ = p[i]
    for j in range(i, N):
        if p[j] > max_:
            max_ = p[j]
        if p[j] < min_:
            min_ = p[j]
        if abs(max_ - min_) == abs(i - j):
            result += 1

print(result)
