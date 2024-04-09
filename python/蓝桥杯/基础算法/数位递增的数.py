n = int(input())


def judge(i_):
    i_str = str(i)
    i_list = list(i_str)
    i_list.sort()
    i_sort = "".join(i_list)
    if i_sort == i_str:
        return True
    else:
        return False


count = 0
for i in range(1, n + 1):
    if judge(i):
        count += 1
print(count)
