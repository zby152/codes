fib = [0, 2, 3, 5, 8, 13]

for _ in range(20):
    fib.append(fib[-1] + fib[-2])

n = int(input())

result = 0.0
for i in range(1, n + 1):
    result += fib[i] / fib[i + 1]

result = format(result, '.5f')
print(result)
