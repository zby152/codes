import heapq

M, MAX_D, N = 10010, 10010, 10010
idx = 0

e = [0 for _ in range(M)]  # e[i]=j 边i的终点是j
h = [-1 for _ in range(N)]  # 起点是i的边的编号是j
w = [0 for _ in range(M)]  # w[i]=j边i的权重是j
ne = [0 for _ in range(M)]  # ne[i]=j 上一条边的编号


def add(start, end, weight):
    global idx
    e[idx] = end
    w[idx] = weight
    ne[idx] = h[start]
    h[start] = idx
    idx+=1


n, m = map(int, input().split())

ind = [0 for _ in range(n + 1)]
begin = []
to = []
for _ in range(n - 1):
    x, y = map(int, input().split())
    ind[x] += 1
    ind[y] += 1
    begin.append(x)
    to.append(y)

for i in range(len(begin)):
    add(begin[i], to[i], ind[begin[i]])
    add(to[i], begin[i], ind[to[i]])


def BFS(start, end, dist, vis):
    hq = []
    heapq.heappush(hq, [0, start])  # [距离,当前点]
    dist[start] = 0
    while len(hq):
        d, t = heapq.heappop(hq)  # t是当前节点
        if t == end:
            break
        else:
            i = h[t]  # i是当前处理到的边的编号
            while i != -1:
                j = e[i]  # j是当前边的终点
                newd = d + w[i]
                if newd <= dist[j]:
                    dist[j] = newd
                    if not vis[j]:
                        heapq.heappush(hq, [dist[j], j])
                i = ne[i]
        vis[t] = 1
    return dist[end]


for _ in range(m):
    u, v = map(int, input().split())
    dist = [MAX_D for _ in range(N)]
    vis = [0 for _ in range(N)]
    ans = BFS(u, v, dist, vis) + ind[v]
    print(ans)
