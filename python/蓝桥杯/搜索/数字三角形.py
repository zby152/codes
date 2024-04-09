N=int(input())
maps=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    maps.append(temp)

max_w=0

mem=[[[[0]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]

def dfs(i,j,l,r):
    global max_w
    ans=0
    if mem[i][j][l][r]:
        return mem[i][j][l][r]
    if i==N-1:
        if abs(l-r)>1:
            return -10000
    else:
        left=dfs(i+1,j,l+1,r)+maps[i+1][j]
        right=dfs(i+1,j+1,l,r+1)+maps[i+1][j+1]
        ans=max(left,right)
    mem[i][j][l][r]=ans
    return ans

res=dfs(0,0,0,0)+maps[0][0]
print(res)
