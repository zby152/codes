direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n = int(input())
for _ in range(n):
    position = [0, 0]
    di = 0
    path = input()
    num_str = ''
    index = 0

    while index < len(path):
        if path[index] == 'L':
            di = (di - 1) % 4
        elif path[index] == 'R':
            di = (di + 1) % 4
        else:
            while index < len(path) and path[index].isdigit():
                num_str = num_str + path[index]
                index += 1
            num = int(num_str)

            position[0] = position[0] + direc[di][0] * num
            position[1] = position[1] + direc[di][1] * num

            index -= 1
            num_str = ''
        index += 1
    dis = pow(abs(position[0]) ** 2 + abs(position[1]) ** 2, 0.5)
    print(format(dis, '.2f'))

"""
5
L100R50R10
3LLL5RR4L12
LL
100R
5L5L5L5
"""
