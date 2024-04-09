# 刚开始想到的是多个目标的广搜
# 正确的思想是将目标放在没有清扫的区域上按顺序处理
# 一个一个地遍历t时间复杂度会很高，这里因为t越大越能够满足条件即具有单调性，用二分搜索


def clean(t, n, k, s):
    clean_p = 0  # 初始清洁位置
    for i in range(k):
        time = t
        if s[i] > clean_p:  # 如果左边有可以扫的区域
            time = time - 2 * (s[i] - clean_p - 1)

        if time < 0:
            return False
        clean_p = s[i] + time // 2  # 这里将剩下的时间用来清扫机器人的右边
    if clean_p >= n:
        return True


(N, K) = map(int, input().split())  # N个格子，K个机器人
start = []
for _ in range(K):
    start.append(int(input()))
start.sort()

front = 0
tail = N * 2

ans = 0
while front <= tail:
    mid = (front + tail) // 2
    if clean(mid, N, K, start):
        ans = mid
        tail = mid - 1
    else:
        front = mid + 1

print(ans)
