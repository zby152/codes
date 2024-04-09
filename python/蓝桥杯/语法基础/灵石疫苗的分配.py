(N, D) = map(int, input().split())

b = input().split()
a = []
for str in b:
    num = int(str)
    a.append(num)

danger = 0
undanger = 0

for number in a:
    if number >= 80 or number <= 9:
        danger += 1
    else:
        undanger += 1

day = 0
while danger > 0:
    danger -= D
    day += 1

while undanger > 0:
    undanger -= D
    day += 1

print(day)
