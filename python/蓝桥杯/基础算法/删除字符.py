# 注意把每一种情况都考虑全

string = list(input())
t = int(input())
j = 0

while t != 0:
    if j + t + 1 > len(string):
        for _ in range(t):
            string.pop(-1)
            t -= 1
        break
    else:
        s = string[j:j + t + 1]
    ch = min(list(s))
    i = s.index(ch)
    for _ in range(i):
        string.pop(j)
        t -= 1
    j += 1

print("".join(string))
