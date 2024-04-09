from collections import deque

direc=[[1,0],[-1,0],[0,1],[0,-1]]
N=int(input())

def inlaw(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False


photo=[]
for _ in range(N):
    temp=list(input())
    photo.append(temp)

def bfs(sx,sy):
    global vis
    q=deque()
    q.append([sx,sy])
    vis[sx][sy]=1
    res=True

    while len(q)>0:
        x,y=q.popleft()
        
        flag=False
        
        for di in direc:
            nx=x+di[0]
            ny=y+di[1]
            
            if inlaw(nx,ny) and photo[nx][ny]=='.':
                flag=True #真 代表会淹没
            if inlaw(nx,ny) and vis[nx][ny]==0 and photo[nx][ny]=='#':
                vis[nx][ny]=1
                q.append([nx,ny])
        if flag==False:
            res=False # 返回值

    return res
    

ans=0
vis=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        x=photo[i][j]
        if x=='.':
            continue
        else:
            if vis[i][j]==0 and bfs(i,j):
                ans+=1
            
print(ans)
