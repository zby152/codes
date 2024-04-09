# 在有向图中找最大环
# 递归的层数可以设置，重点在于如何将结果保存下来防止二次被计算

import sys
sys.setrecursionlimit(1000000)
ans=0


def DFS(now,path_id,id):
    global ans
    if invited[now] and invited[now]!=id:
        return
    if invited[now]:
        ans=max(ans,path_id-1-numbers[now]+1)
        return
    numbers[now]=path_id
    invited[now]=id
    DFS(e[now],path_id+1,id)


N=int(input())
e=[0]
e_=list(map(int,input().split()))
e.extend(e_)
invited=[0 for _ in range(N+1)]
numbers=[0 for _ in range(N+1)]

for i in range(1,N+1):
    DFS(i,1,i)
    

print(ans)

