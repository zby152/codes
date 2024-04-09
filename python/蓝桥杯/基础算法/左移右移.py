# 多次左移右移操作可以用双指针一个指向负数一个指向正数，最后再按照大小排序

n, m = map(int, input().split())
arr = list(range(n + 1))  # 数据数组, 从a[1]开始不要a[0]
pos = list(range(n + 1))  # 轨迹数组, 从a[1]开始不要a[0]
left = -1  # 左移记录器(确保起始小于所有数)
right = n + 1  # 右移记录器(确保起始大于所有数)

# 开始操作
for _ in range(m):
    opt, x = input().split()
    x = int(x)
    if opt == 'L':
        pos[x] = left  # 把x的位置记录为左移，-n在排序中代表第n个进行左移
        left -= 1
    else:
        pos[x] = right  # 把x的位置记录为右移，k在排序中代表第n - k个进行左移
        right += 1
arr.pop(arr.index(0))  # 记得把a[0]弹掉
arr.sort(key=lambda k: pos[k])
print(' '.join([str(x) for x in arr]))
