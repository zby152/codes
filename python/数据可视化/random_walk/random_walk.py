from random import choice


class RandomWalk():
    """随机生成漫步数据"""

    def __init__(self, num_point=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_point
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """计算步数"""

        # 决定移动的方向和距离
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步知道到达规定最高点
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 不允许原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算移动之后的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
