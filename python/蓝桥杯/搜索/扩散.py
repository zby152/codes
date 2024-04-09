"""
from collections import deque
N=8000
d=3000#偏移量
direc=[[1,0],[-1,0],[0,1],[0,-1]]

q=deque()
q.append([0+d,0+d,0])
q.append([2020+d,11+d,0])
q.append([11+d,14+d,0])
q.append([2000+d,2000+d,0])

blacks=[[0] * N for _ in range(N)]
blacks[0+d][0+d]=1
blacks[2020+d][11+d]=1
blacks[11+d][14+d]=1
blacks[2000+d][2000+d]=1
ans=4

while q:
    x,y,t=q.popleft()
    if t==2020:
        continue
    for di in direc:
        nx=x+di[0]
        ny=y+di[1]
        if blacks[nx][ny]==0:
            blacks[nx][ny]=1
            q.append([nx,ny,t+1])
            ans+=1

print(ans)
"""
print("20312088")
