import copy

n = int(input())
D = []
for _ in range(n):
    a, b = map(int, input().split())
    D.append([2 * a, 2 * b])

D.sort(key=lambda x: x[1])


def check(m):
    np = copy.deepcopy(D)
    k = 0
    while True:
        flag = 0
        for i in range(len(np)):
            if np[i][0] - m <= k and k <= np[i][1] + m:
                flag = 1
                if np[i][0] + m >= k:
                    k = k + np[i][1] - np[i][0]
                else:
                    k = np[i][1] + m
                np.pop(i)
                break
        if k >= 20000 or flag == 0:
            break
    return k >= 20000


l = 0
r = 20000
ans = 0
while l < r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid
    else:
        l = mid + 1

if ans / 2 == ans // 2:
    print(ans // 2)
else:
    print(round(ans / 2, 1))
