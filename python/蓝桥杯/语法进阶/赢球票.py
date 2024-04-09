N = int(input())
card_init = list(map(int, input().split()))

max_count = 0
for start in range(N):
    card = card_init.copy()
    invited = [0 for _ in range(N)]
    count = 0
    i = start
    j = 1
    while len(card) > 0 and j <= N and 0 in invited:
        if card[i % len(card)] == j and invited[i] == 0:
            count += card[i % len(card)]
            invited[i] = 1
            j = 1

        elif invited[i] == 0:
            j += 1
        i = (i + 1) % N
    if count > max_count:
        max_count = count

print(max_count)
