import matplotlib.pyplot as plt

# s是点的尺寸
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# edgecolor去掉数据点的黑色轮廓 c表示数据点的颜色列表,cmap使用蓝色进行映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题和坐标轴标题
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设计标记刻度的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
