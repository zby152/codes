# 标准差只需要保证每个数距离平均数的差最小，
# 维护一个动态的平均数，每次新加入的人都距离这个平均数最小，最后总的标准差最小
n, s = map(int, input().split())
a = list(map(int, input().split()))

avg = s / n
a.sort()
ans = 0

for i in range(n):
    if a[i] * (n - i) < s:
        ans += (a[i] - avg) ** 2
        s -= a[i]
    else:
        cur = s / (n - i)
        ans += (cur - avg) ** 2 * (n - i)
        break

ans = pow(ans / n, 0.5)

print(format(ans, ".04f"))
