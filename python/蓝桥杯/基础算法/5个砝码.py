def find_(n):
    way = [-1, 0, 1]
    for num1 in way:
        for num2 in way:
            for num3 in way:
                for num4 in way:
                    for num5 in way:
                        number = num1 * 1 + num2 * 3 + num3 * 9 + num4 * 27 + num5 * 81
                        if number == n:
                            return num1, num2, num3, num4, num5


def print_(op, num):
    if op == 1:
        print("+" + str(num), end="")
    if op == -1:
        print("-" + str(num), end="")


N = int(input())
ops = list(find_(N))
numbers = [1, 3, 9, 27, 81]
start = 0
for i in range(4, -1, -1):
    if ops[i] != 0:
        start = i
        break
print(numbers[start], end="")
for i in range(start - 1, -1, -1):
    print_(ops[i], numbers[i])
