# flody算法和二分搜索相结合
# 求解所有点对之间的最短距离问题

import copy

n, Q = map(int, input().split())
d = []
for i in range(n):
    temp = list(map(int, input().split()))
    d.append(temp)
m = []
for i in range(n):
    temp = list(map(int, input().split()))
    m.append(temp)


def floyd(dis):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    return sum(sum(x) for x in dis)


def check(day):
    x = day // n  # 所有城市共同的
    y = day % n  # 最后一圈剩下的
    temp_dis = copy.deepcopy(d)
    for i in range(n):
        for j in range(n):
            if i < y:
                temp_dis[i][j] = max(m[i][j], temp_dis[i][j] - 1-x)
            else:
                temp_dis[i][j] = max(m[i][j], temp_dis[i][j] - x)  # 注意在两个城市共同维护一条街道，所以前面的街道减了之后后面的街道也要减自己
            temp_dis[j][i] = temp_dis[i][j]
    return floyd(temp_dis) <= Q


if __name__ == "__main__":
    t = copy.deepcopy(m)
    if floyd(t) > Q:
        print(-1)
    else:
        l = 0
        r = 10000000  # 注意压缩一下
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        print(ans)
