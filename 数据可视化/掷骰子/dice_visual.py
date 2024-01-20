from die import Die
import pygal

# 创建一个6面骰子
die_1 = Die(6)
die_2 = Die(10)

# 投掷骰子100次
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 统计投掷骰子的结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 创建一个直方图
hist = pygal.Bar()
hist.title = "Result of rolling D6 100 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 将值添加到图表中
hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual.svg')
