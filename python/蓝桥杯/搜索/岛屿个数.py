T=int(input())
direc=[[1,0],[-1,0],[0,1],[0,-1]]
direc_sea=[[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
from collections import deque

def inlaw(x,y):
    global M,N
    if x>=0 and x<M and y>=0 and y<N:
        return True
    else:
        return False

def dfs(x,y,sx,sy,num):
    global vis,cir
    if x==sx and y==sy:
        return True
    
    for di in direc:
        nx=x+di[0]
        ny=y+di[1]
        if inlaw(nx,ny) and vis[nx][ny]==0 and maps[nx][ny]==1:
            vis[nx][ny]=num
            dfs(nx,ny,sx,sy,num)
    return False



def bfs(x,y):
    q.clear()
    viss=[[0]*N for _ in range(M)]
    for di in direc_sea:
        nx=x+di[0]
        ny=y+di[1]
        if (nx==-1 or ny==-1 or nx==M or ny==N)or (inlaw(nx,ny) and maps[nx][ny]==0 and viss[nx][ny]==0):
            q.append([nx,ny])
    while q:
        i,j=q.popleft()
        if i==-1 or j==-1 or i==M or j==N:
            return True
        for di in direc_sea:
            ni=i+di[0]
            nj=j+di[1]
            if ni==-1 or nj==-1 or ni==M or nj==N:
                return True
            if inlaw(ni,nj) and maps[ni][nj]==0 and viss[ni][nj]==0:
                viss[ni][nj]=1
                q.append([ni,nj])
    return False
    

for _ in range(T):
    maps=[]
    num=1
    M,N=map(int,input().split())
    for _ in range(M):
        temp=list(map(int,input()))
        maps.append(temp)

    vis=[[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if maps[i][j]==1 and vis[i][j]==0:
                vis[i][j]=num
                for di in direc:
                    ni=i+di[0]
                    nj=j+di[1]
                    if inlaw(ni,nj) and vis[ni][nj]==0 and maps[ni][nj]==1:
                        vis[ni][nj]=num
                        flag=dfs(ni,nj,i,j,num)
                num+=1
    n=1
    ans=0
    q=deque()
    for n in range(1,num):
        flag=0
        for i in range(M):
            for j in range(N):
                if vis[i][j]==n:
                    if bfs(i,j):
                        ans+=1
                        n+=1
                        flag=1
                if flag==1:
                    break
            if flag==1:
                break
    print(ans)



"""
1
5 6
111111
100001
010101
100001
111111
"""                
