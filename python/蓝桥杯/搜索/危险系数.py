# 图的DFS

count=0
flag=1


def get_end(x):
    global count,V,invited,flag
    if flag==0:
        return
    if x==V:
        count+=1
        flag=0
    else:
        for y in e[x]:
            if invited[y]==0:
                invited[y]=1
                get_end(y)
                invited[y]=0


(n,m)=map(int,input().split())
e=[[]for _ in range(n+1)]
for _ in range(m):
    (u,v)=map(int,input().split())
    e[u].append(v)
    e[v].append(u)

(U,V)=map(int,input().split())
invited=[0 for _ in range(n+1)]

for i in range(1,n+1):
    if i!=U and i!=V:
        flag=1
        temp=e[i].copy()
        e[i]=[]
        invited[U]=1
        invited[i]=1
        get_end(U)
        invited[i]=0
        e[i]=temp.copy()

print(n-count-2)
