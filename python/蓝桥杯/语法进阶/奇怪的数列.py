def round_(num_str):
    result = []
    i = 0
    sumx = 1

    while i < len(num_str):
        if i == 0:
            i += 1
        if i < len(num_str):

            if num_str[i] == num_str[i - 1]:
                sumx += 1
            else:
                temp = [sumx, int(num_str[i - 1])]
                result.append(temp)
                sumx = 1

        if i == len(num_str) - 1:
            temp = [sumx, int(num_str[i])]
            result.append(temp)
        if i == len(num_str):
            temp = [sumx, int(num_str[i - 1])]
            result.append(temp)

        i += 1

    result_str = ""
    for temp in result:
        result_str = result_str + str(temp[0]) + str(temp[1])

    return result_str


num_string = input()
n = int(input())

# num_string="5"
# n=7
for _ in range(n):
    round_res = round_(num_string)
    num_string = round_res
print(round_res)
