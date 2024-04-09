direc=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
n=0
m=0

def in_map(x,y):
    if x>=0 and y>=0 and x<n and y<m:
        return True
    else:
        return False


(n,m)=map(int,input().split())

maps=[]
n_map=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    maps.append(temp)

for i in range(n):
    temp_result=[]
    for j in range(m):
        count=0
        sum=0
        for d in direc:
            next_x=i+d[0]
            next_y=j+d[1]
            if in_map(next_x,next_y):
                count+=1
                sum+=maps[next_x][next_y]
        result=sum//count
        temp_result.append(result)
    n_map.append(temp_result)

for i in range(n):
    for j in range(m):
        print(n_map[i][j],end=' ')
    if i <n-1:
        print()
    
                
