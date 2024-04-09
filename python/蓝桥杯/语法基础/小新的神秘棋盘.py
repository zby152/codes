T=int(input())

maps=[[2 for _ in range(9)] for _ in range(9)]
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            maps[i][j]=0
        else:
            maps[i][j]=1

for _ in range(T):
    (a,b,p,q)=map(int,input().split())
    source=maps[a][b]
    target=maps[p][q]
    if a==p and b==q:
        print(0)
    elif source==target:
        print(2)
    else:
        print(1)
    

##[[2, 2, 2, 2, 2, 2, 2, 2, 2],
## [2, 0, 1, 0, 1, 0, 1, 0, 1],
## [2, 1, 0, 1, 0, 1, 0, 1, 0],
## [2, 0, 1, 0, 1, 0, 1, 0, 1],
## [2, 1, 0, 1, 0, 1, 0, 1, 0],
## [2, 0, 1, 0, 1, 0, 1, 0, 1],
## [2, 1, 0, 1, 0, 1, 0, 1, 0],
## [2, 0, 1, 0, 1, 0, 1, 0, 1],
## [2, 1, 0, 1, 0, 1, 0, 1, 0]]
