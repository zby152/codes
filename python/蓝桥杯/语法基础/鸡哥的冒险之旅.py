def find_min(now_i, now_j):
    min_di = [0, 0]
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for di in directions:
        if now_i + di[0] >= N or now_j + di[1] >= M or now_i + di[0] <0 or now_j + di[1] <0:
            continue
        if magic[now_i + di[0]][now_j + di[1]] < magic[now_i + min_di[0]][now_j + min_di[1]]:
            min_di = di
    return min_di


(N, M) = map(int, input().split())

magic = []
for _ in range(N):
    m = list(map(int, input().split()))
    magic.append(m)

numbers = [[1 for _ in range(M)] for _ in range(N)]
flag = 1
while flag == 1:
    flag = 0
    for i in range(N):
        for j in range(M):
            x, y = find_min(i, j)
            if numbers[i][j] != 0 and (x != 0 or y != 0):
                numbers[i + x][j + y] += numbers[i][j]
                numbers[i][j] = 0
                flag = 1

for i in range(N):
    for j in range(M):
        print(numbers[i][j], end=' ')
    if i != N - 1:
        print()

"""
4 6
95648 25725 36236 38213 5486  99979
88864 7261  98854 88465 44586 97567
65784 16474 87975 57720 68165 6472
82019 47447 106   56822 82375 8724


0 0 0 0 5 0 
0 3 0 0 0 0 
0 0 0 0 0 7 
0 0 9 0 0 0 

"""
