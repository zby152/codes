a = [0 for _ in range(2024)]

for i in range(1, 2024):
    a[i] = i

result = [0 for _ in range(4048)]

for i in range(2, 4047):
    for x in range(1, i):
        y = i - x
        if x <= y and x <= 2023 and y <= 2023:
            if x == y:
                result[i] += int(x // 2)
            else:
                result[i] += min(x, y)
    if i <= 2023:
        result[i] += i

sum_max = max(result)

print(sum_max)
