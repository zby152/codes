import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 读取文件下一行的数据

    # 打印第一行数据中每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # 获取每一天的日期及其最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

# 获取图像数据
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha为颜色的透明度
plt.plot(dates, lows, c='blue', alpha=0.5)

# 填充两条线之间的空隙
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 定义图表的标题和坐标轴等
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=14)

# 将日期标签倾斜，防止重叠
fig.autofmt_xdate()

plt.ylabel("Temperature(F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
