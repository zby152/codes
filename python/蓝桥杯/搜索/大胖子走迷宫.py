from collections import deque

n,k=map(int,input().split())
maps=[list(input()) for i in range(n)]

q=deque()
q.append([2,2,0,2])

vis=[[0]*n for _ in range(n)]
vis[2][2]=1

direc=[[1,0],[-1,0],[0,1],[0,-1]]

def inlaw(x,y,f):
    for i in range(x-f,x+f+1):
        for j in range(y-f,y+f+1):
            if maps[i][j]=="*":
                return False
    return True

def get_fat(time):
    if time < k:
        return 2
    if time <2*k:
        return 1
    else:
        return 0

def bfs():
    while len(q)>0:
        x,y,t,fat=q.popleft()
        if x==n-3 and y==n-3:
            return t
        if fat>0:
            q.append([x,y,t+1,get_fat(t+1)])
        for di in direc:
            nx=x+di[0]
            ny=y+di[1]
            if nx-fat>=0 and nx+fat<n and ny-fat>=0 and ny+fat<n and vis[nx][ny]==0:
                if inlaw(nx,ny,fat):
                    vis[nx][ny]=1
                    q.append([nx,ny,t+1,get_fat(t+1)])
print(bfs())
