import matplotlib.pyplot as plt

# 向plot提供列表使其绘制出合适的图形
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 图表的标题
plt.title("Square Numbers", fontsize=24)

# 坐标轴的标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度样式 axis样式影响到所有
plt.tick_params(axis='both', labelsize=14)

plt.show()
