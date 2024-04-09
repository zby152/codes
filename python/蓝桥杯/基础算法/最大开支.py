# 堆相关
import heapq

N = 1000010

k = [0 for _ in range(N)]
b = [0 for _ in range(N)]
people = [0 for _ in range(N)]  # 每个项目的人数


def cacul(x, i):
    # 第i个项目有x个人求得总花费
    res = x * max(k[i] * x + b[i], 0)
    return res


n, m = map(int, input().split())
pq = []

# 计算每个项目一个人的情况，并生成一个大根堆，
for i in range(m):
    k[i], b[i] = map(int, input().split())
    people[i] = 1
    money = cacul(1, i)
    heapq.heappush(pq, (-money, i))

ans = 0
while len(pq) > 0 and n > 0:
    p = heapq.heappop(pq)
    w, i = -p[0], p[1]  # w表示能够创造的价值
    if w < 0:  # 最能够创造价值的已经不能够创造价值
        break
    ans += w
    money1 = cacul(people[i] + 1, i)
    money2 = cacul(people[i], i)
    heapq.heappush(pq, (-(money1 - money2), i))  # 当前新加入的这个人所带来的收益的变化
    people[i] += 1
    n -= 1
print(ans)
