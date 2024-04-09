def sqrt(x):
    """找到小于x的所有的平方数"""
    L = 1
    R = x
    ans=0
    while L <= R:
        mid = (L + R) // 2
        if mid ** 2 > x:
            R = mid - 1
        else:
            L = mid+1
            ans=mid
    return ans


n, m = map(int, input().split())

print(sqrt(n) * sqrt(m))
