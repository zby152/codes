f = [1, 1]

for i in range(2, 61):
    temp = (f[i - 1] + f[i - 2]) % 10
    f.append(temp)

round = 202202011200 // 60
last = 202202011200 % 60

la = 0
for i in range(last):
    if f[i] == 7:
        la += 1

ans = round * 8 + la
print(ans)
