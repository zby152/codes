def short(x):
    while x >= 10:
        x_str = str(x)
        sum = 0
        for i in x_str:
            sum += int(i)
        x = sum

    return x


number = int(input())
result = short(number)

print(result)
