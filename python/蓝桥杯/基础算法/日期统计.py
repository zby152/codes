# 日期相关问题
# 注意子序列的定义
# 拿着答案去匹配不同情况的解题思维

from datetime import datetime, timedelta

data = [5, 6, 8, 6, 9, 1, 6, 1, 2, 4, 9, 1, 9, 8, 2, 3, 6, 4, 7, 7, 5, 9, 5, 0, 3, 8, 7, 5, 8, 1, 5, 8, 6, 1, 8, 3, 0,
        3, 7, 9, 2, 7, 0, 5, 8, 8, 5, 7, 0, 9, 9, 1, 9, 4, 4, 6, 8, 6, 3, 3, 8, 5, 1, 6, 3, 4, 6, 7, 0, 7, 8, 2, 7, 6,
        8, 9, 5, 6, 5, 6, 1, 4, 0, 1, 0, 0, 9, 4, 8, 0, 9, 1, 2, 8, 5, 0, 2, 5, 3, 3]

cnt = 0
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 12, 31)

for i in range(365):
    date_now = date1 + timedelta(days=i)
    date_str = date_now.strftime("%Y%m%d")

    k = 0
    flag = 0
    while k < 100:
        if str(data[k]) == date_str[flag]:
            flag += 1
        if flag == 8:
            cnt += 1
            break
        k += 1

print(cnt)
