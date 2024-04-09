# 贪心，排序

def fun(x):
    return x[0], x[1]


n = int(input())
final_times = n // 10
numbers = []
count = [[] for _ in range(10)]  # count表示每一个数的所有修改代价
for _ in range(n):
    a, b = map(int, input().split())
    count[a].append(b)

m_or_l = [0 for _ in range(10)]
for i in range(10):
    m_or_l[i] = len(count[i]) - final_times
    count[i].sort()

sum = 0
for i in range(10):
    while m_or_l[i] > 0:
        x = count[i].pop(0)
        sum += x
        m_or_l[i] -= 1

print(sum)
