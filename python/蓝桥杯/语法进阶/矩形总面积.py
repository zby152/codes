(x1, y1, x2, y2, x3, y3, x4, y4) = map(int, input().split())

a1 = x2 - x1
b1 = y2 - y1

a2 = x4 - x3
b2 = y4 - y3

s1 = a1 * b1
s2 = a2 * b2

if x3 > x2 or x1 > x4 or y3 > y2 or y1 > y4:
    s3 = 0
else:
    a = min(x2, x4) - max(x3, x1)
    b = min(y2, y4) - max(y3, y1)
    s3 = abs(a) * abs(b)

s = s1 + s2 - s3
print(s)
