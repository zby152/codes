def short(x):
    while x >= 10:
        x_str = str(x)
        sum = 0
        for i in x_str:
            sum += int(i)
        x = sum

    return x


n = int(input())

for _ in range(n):
    string = input()
    str_list = []
    string_6 = ""
    for i, ch in enumerate(string):
        string_6 = string_6 + ch
        if (i + 1) % 6 == 0:
            str_list.append(string_6)
            string_6 = ""
    if len(string_6) != 0:
        str_list.append(string_6)

    numbers = [0, 0, 0, 0, 0, 0]
    for string in str_list:
        for i, ch in enumerate(string):
            numbers[i] += ord(ch)

    result = ""
    for number in numbers:
        result = result + str(short(number))

    print("".join(result))
