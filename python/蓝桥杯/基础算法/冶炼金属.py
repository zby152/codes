# 二分搜索定范围可以先找到一个解之后再由其向两边拓展

def check(midd, a, b):
    for i in range(len(a)):
        if (a[i] // midd) > b[i]:
            return 2  # v的值太小了
        elif (a[i] // midd) < b[i]:
            return 1  # 太大了
    return 0  # 可以


N = int(input())
o = []
x = []
for _ in range(N):
    A, B = map(int, input().split())
    o.append(A)
    x.append(B)

front = 0
tail = max(o)
ans = 0
while front <= tail:
    mid = (front + tail) // 2
    flag = check(mid, o, x)
    if flag == 2:
        front = mid + 1
    elif flag == 1:
        tail = mid - 1
    else:
        ans = mid
        break

min_ans = ans
max_ans = ans
while True:
    if check(min_ans - 1, o, x) == 0:
        min_ans -= 1
    else:
        break

while True:
    if check(max_ans + 1, o, x) == 0:
        max_ans += 1
    else:
        break

print(min_ans, end=" ")
print(max_ans)
