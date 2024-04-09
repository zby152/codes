# round保留第n位的四舍五入结果

n = int(input())

scores = []
good = 0
best = 0
for _ in range(n):
    score = int(input())
    if score >= 60:
        good += 1
    if score >= 85:
        best += 1
    scores.append(score)

good_rate = int(round(100 * good / n, 0))
best_rate = int(round(100 * best / n, 0))

print(str(good_rate) + "%")
print(str(best_rate) + "%")
