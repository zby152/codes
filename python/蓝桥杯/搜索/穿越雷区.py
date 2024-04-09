from collections import deque


def judge(x, y):
    global n
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    else:
        return False


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n = int(input())
maps = []
for i in range(n):
    temp = list(input().split())
    if "A" in temp or "B" in temp:
        for j in range(len(temp)):
            if temp[j] == "A":
                s_x = i
                s_y = j
            if temp[j] == "B":
                e_x = i
                e_y = j
    maps.append(temp)
invited = [[0 for _ in range(n)] for _ in range(n)]

q = deque()
q.append([s_x, s_y, "x", 0])  # x,y,+ -，步数
invited[s_x][s_y] = 1

while len(q) > 0:
    temp = q.popleft()
    x, y, w, step = temp[0], temp[1], temp[2], temp[3]

    if x == e_x and y == e_y:
        print(step)
        break
    else:
        for di in directions:
            n_x = x + di[0]
            n_y = y + di[1]
            if judge(n_x, n_y) and invited[n_x][n_y] == 0:
                n_w = maps[n_x][n_y]
                if n_w != w:
                    q.append([n_x, n_y, n_w, step + 1])
                    invited[n_x][n_y] = 1
