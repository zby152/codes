n,m,x=map(int,input().split())
a=[0]+list(map(int,input().split()))
pos=[0]*(n+10)
mp={}
for i in range(1,n+1):
    y=x^a[i]
    if mp.get(y):
        pos[i]=max(pos[i-1],mp[y])
    else:
        pos[i]=max(pos[i-1],0)
    mp[a[i]]=i
res=[]
for i in range(m):
    L,R=map(int,input().split())
    if pos[R]>=L:
        res.append('yes')
    else:
        res.append('no')
for i in range(m):
    print(res[i])


