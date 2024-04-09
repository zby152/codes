n = int(input())
(a, b, c) = map(int, input().split())

res = 0
for i in range(1, n + 1):
    if i % a != 0 and i % b != 0 and i % c != 0:
        res += 1

print(res)
