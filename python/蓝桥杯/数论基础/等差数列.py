# 一维差分，注意除零报错
N = int(input())
a = list(map(int, input().split()))

a.sort()
q = [a[0]]
for i in range(1, N):
    q.append(a[i] - a[i - 1])
d = min(q[1:])
ans = N
if d==0:
    print(N)
else:
    for j in range(1, N):
        ans += q[j] // d - 1
    print(ans)
