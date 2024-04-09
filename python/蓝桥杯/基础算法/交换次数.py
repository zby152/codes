# 思维类型题，只要把前两个交换完就不用管第三个，所以考虑问题的时候只需要考虑前两个

start = list(input())
cnt = {"A": 0, "B": 0, "T": 0}
cnt["A"] = start.count("A")
cnt["B"] = start.count("B")
cnt["T"] = start.count("T")

res = ["ABT", "BAT", "ATB", "BTA", "TAB", "TBA"]

ans = len(start)
for i in range(6):
    x = res[i]
    n1 = cnt[x[0]]
    n2 = cnt[x[1]]
    n3 = cnt[x[2]]
    p = -1
    wrong = 0
    wrong_21 = 0
    wrong_12 = 0
    for num1 in range(n1):
        p += 1
        if start[p] != x[0]:
            wrong += 1
        if start[p] == x[1]:
            wrong_21 += 1

    for num2 in range(n2):
        p += 1
        if start[p] != x[1]:
            wrong += 1
        if start[p] == x[0]:
            wrong_12 += 1

    times = wrong - min(wrong_21, wrong_12)
    ans = min(ans, times)

print(ans)
