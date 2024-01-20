import random

# 输出一个0.0-1.0的随机小数
random_number = random.random()
print(random_number)

# 输出一个从0-9的随机整数
print(random.randint(0, 9))

# 从给出的列表中选择一个进行输出
list1 = [1, 2, 3, 4]
random_element = random.choice(list1)
print(random_element)

# 将给出的列表进行随机排序
list2=[1,2,3,4,5]
random.shuffle(list2)
print(list2)

