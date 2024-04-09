(N, M) = map(int, input().split())

bad_balls = []
god_water = {}

for i in range(M):
    K = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    weight = input()
    if weight == "<":
        if len(bad_balls) != 0:
            bad_balls = list(set(left) & set(bad_balls))
        else:
            bad_balls = left.copy()

    elif weight == ">":
        if len(bad_balls) != 0:
            bad_balls = list(set(right) & set(bad_balls))
        else:
            bad_balls = right.copy()

    else:
        bad_balls = list(set(bad_balls) - set(left) - set(right))
        for i in left:
            god_water[i] = 1
        for j in right:
            god_water[j] = 1

if (len(bad_balls) > 0):
    print(len(bad_balls))
else:
    print(N - len(god_water))
