# 二分搜索
def check(x):
    buf = m
    for i in range(n):
        if a[i] >= x:
            continue
        else:
            need = x - a[i]
            if need > buf or need > b[i]:
                return False
            else:
                buf = buf - need
    return True


n, m = map(int, input().split())
a = list(map(int, input().split()))  # 每种牌的数量
b = list(map(int, input().split()))  # 每种牌最多可补多少

l = 0
r = 4 * n
ans = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1
print(ans)
