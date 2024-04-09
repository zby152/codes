direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direc_str = ["U", "R", "D", "L"]
m = 0
n = 0
di = 0


def inmap(x, y):
    if x >= 0 and y >= 0 and x < m and y < n:
        return True
    else:
        return False


(m, n) = map(int, input().split())

maps = []
for _ in range(m):
    temp = list(map(int, input().split()))
    maps.append(temp)

(x, y, s, k) = input().split()
x = int(x)
y = int(y)
k = int(k)

for i in range(4):
    if direc_str[i] == s:
        di = i

for times in range(k):
    if maps[x][y] == 0:
        di = (di - 1) % 4
        maps[x][y] = 1
        x = x + direc[di][0]
        y = y + direc[di][1]
    else:
        di = (di + 1) % 4
        maps[x][y] = 0
        x = x + direc[di][0]
        y = y + direc[di][1]

print(str(x) + " " + str(y))
