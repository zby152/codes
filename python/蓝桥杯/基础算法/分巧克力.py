# 二分搜索算法

H = []
W = []


def find(length):
    n = 0
    for i in range(N):
        a = H[i] // length
        b = W[i] // length
        n = n + a * b
    if n >= K:
        return True
    else:
        return False


(N, K) = map(int, input().split())

S = 0
for _ in range(N):
    (Hi, Wi) = map(int, input().split())
    H.append(Hi)
    W.append(Wi)
    S = S + Wi * Hi

max_s = S // K
max_a = int(pow(max_s, 0.5))

front = 1
tail = max_a

while (front <= tail):
    mid = (front + tail) // 2
    if (not find(mid)):
        tail = mid - 1
    else:
        front = mid + 1

print(tail)
