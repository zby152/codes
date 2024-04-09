light=[0]*7
connect=[[1,5],[0,2,6],[1,3,6],[2,4],[3,5,6],[0,4,6],[1,2,4,5]]
from collections import deque

def check(l):
    q=deque()
    vis=[0]*7
    num=0
    for i in range(7):
        if l[i]==1:
            q.append(i)
            vis[i]=1
            break
        num+=1
    while q:
        x=q.popleft()
        for nx in connect[x]:
            if vis[nx]==0 and l[nx]==1:
                q.append(nx)
                vis[nx]=1
    for i in range(7):
        if vis[i]!=l[i]:
            return False
    if num==7: return False
    return True
            

ans=0
def dfs(i):
    global light,ans
    if i==7 and check(light):
        ans+=1
        return
    if i==7:
        return 
    else:
        dfs(i+1)
        light[i]=1
        dfs(i+1)
        light[i]=0

dfs(0)
print(ans)

