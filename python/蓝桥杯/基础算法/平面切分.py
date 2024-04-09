lines = []


def get_point(k1, b1, k2, b2):
    a = (b1 - b2) / (k2 - k1)
    b = (k1 * b2 - k2 * b1) / (k1 - k2)
    return [a, b]


N = int(input())
lines = []
res = 1
for _ in range(N):
    points = []
    (Ai, Bi) = map(int, input().split())
    if [Ai, Bi] in lines:
        continue

    for line in lines:
        if line[0] != Ai:
            new_point = get_point(Ai, Bi, line[0], line[1])
            if new_point not in points:
                points.append(new_point)
    res = res + len(points) + 1
    lines.append([Ai, Bi])

print(res)
