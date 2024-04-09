(n, m) = map(int, input().split())

towers = []
for _ in range(n):
    temp = list(map(int, input().split()))
    for x in temp:
        towers.append(x)
towers.sort(reverse=True)
while towers[-1] == 0:
    towers.pop()

H = int(input())
number = 0

for h in range(1, H + 1):
    number += len(towers)
    while len(towers) and towers[-1] <= h:
        towers.pop()

    print(number)
