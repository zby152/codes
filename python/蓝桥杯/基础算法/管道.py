MAX_T = 2000000000
n, LEN = map(int, input().split())

op = []
for _ in range(n):
    l, s = map(int, input().split())
    op.append([l, s])

def check(t):  # 不需要对于所有的单元管道进行遍历，只需要保留一个最右侧水位就行
    v = []
    for i in range(n):
        water = op[i]
        if water[1] <= t:
            v.append([water[0] - (t - water[1]), water[0] + (t - water[1])])
    v.sort()
    if len(v)==0 or v[0][0]>1:
        return False
    r = v[0][1]  # 最右侧能够满上的水位
    for i in range(len(v)):
        if v[i][0]<=r+1:
            r=max(v[i][1],r)
        else:
            break
    return r>=LEN




front = 0
right = MAX_T
ans = right
while front <= right:
    mid = (front + right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        front = mid + 1
print(ans)
