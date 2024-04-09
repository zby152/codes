def rule1(x):
    num1 = int(x[0])
    num2 = int(x[1])
    num3 = int(x[2])
    num4 = int(x[3])

    if num1 + 1 == num2 and num2 + 1 == num3 and num3 + 1 == num4:
        return 5
    if num1 == num2 + 1 and num2 == num3 + 1 and num3 == num4 + 1:
        return 5
    return 0


def rule2(x):
    num1 = x[0]
    num2 = x[1]
    num3 = x[2]
    num4 = x[3]
    result = 0
    if num1 == num2 and num2 == num3:
        result += 3
    if num2 == num3 and num3 == num4:
        result += 3

    return result


def rule3(x):
    num1 = x[0]
    num2 = x[1]
    num3 = x[2]
    num4 = x[3]
    result = 0
    if num1 == num2 and num3 == num4:
        result += 1
    if num1 == num3 and num2 == num4:
        result += 1
    return result


def rule4(x):
    result = 0

    for ch in x:
        if ch == "6" or ch == "8" or ch == "9":
            result += 1
    return result


n = int(input())
for _ in range(n):
    numbers = input()
    score1 = rule1(numbers)
    score2 = rule2(numbers)
    score3 = rule3(numbers)
    score4 = rule4(numbers)
    score = score1 + score2 + score3 + score4
    print(score)
