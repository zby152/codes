T=int(input())


def dfs(x,r,cnt):
    global TS,TE,L,N,plane,vis

    if TE[x]<r:
        return False
    if cnt==N:
        return True
    
    for y in range(N):
        if vis[y]==0:
            vis[y]=1
            if dfs(y,max(r,TS[x])+L[x],cnt+1):
                return True
            vis[y]=0
    return False
            

for _ in range(T):
    N=int(input())
    TS=[]
    TE=[]
    L=[]
    res="NO"
    for _ in range(N):
        t,d,l=map(int,input().split())
        TS.append(t)
        TE.append(t+d)
        L.append(l)
        

    for i in range(N):
        vis=[0]*N
        vis[i]=1
        if dfs(i,0,1):
            res="YES"
            break
    print(res)
