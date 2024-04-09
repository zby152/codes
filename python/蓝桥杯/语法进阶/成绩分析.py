def max_score(s):
    max_s = 0
    for score in s:
        if score > max_s:
            max_s = score

    return max_s


def min_score(s):
    min_s = 100
    for score in s:
        if score < min_s:
            min_s = score

    return min_s


def sum_score(s):
    sum = 0
    for score in s:
        sum += score

    result = sum / len(s)
    result = format(result, '.2f')
    return result


n = int(input())
score = []

for _ in range(n):
    temp = int(input())
    score.append(temp)

max_score = max_score(score)
min_score = min_score(score)
sum_score = sum_score(score)

print(max_score)
print(min_score)
print(sum_score)
