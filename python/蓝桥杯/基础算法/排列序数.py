def n_1(n):
    sum_ = 1
    for i in range(1, n + 1):
        sum_ = sum_ * i
    return sum_


string = list(input())
stri = sorted(string)
N = len(stri)

count = 0
for i, ch in enumerate(string):
    for j, s in enumerate(stri):
        if s == ch:
            count = count + j * n_1(N - i - 1)
            stri.pop(j)
            break

print(count)
