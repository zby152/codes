import matplotlib.pyplot as plt
from codes.数据可视化.random_walk.random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 定义输出框的尺寸
    plt.figure(dpi=128,figsize=(10,6))

    # 隐藏坐标轴
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    point_numbers = list(range(rw.num_points))

    # 给漫步的各个点进行着色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # 特殊显示漫步的起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # 隐藏边框
    plt.axis('off')

    plt.show()

    # 持续漫步
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
