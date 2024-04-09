# 字典的用法
# 大数据量的题不能创造太多的无用数据，直接将所有的时间保存下来而不是用滑动窗口，这样可以节省大部分时间和空间

def check(d, k, ts_):
    for x in ts_:
        count = 0
        for y in ts_:
            if x <= y and y < x + d:
                count += 1
            if count >= k:
                return True
    return False


n, d, k = map(int, input().split())

data = dict()
for _ in range(n):
    ts, ids = map(int, input().split())
    data[ids] = data.get(ids, []) + [ts]  # 读入字典将所有时间放入列表中

ans = []
for j in data.items():  # 取字典中的所有元素
    ids, ts_ = (i for i in j)
    ts_ = sorted(ts_)
    if check(d, k, ts_):
        ans.append(ids)

ans.sort()
for i in ans:
    print(i)
