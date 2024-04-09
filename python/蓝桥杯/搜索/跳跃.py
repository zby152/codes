max_=0
ways=[[1,0],[2,0],[3,0],[0,1],[1,1],[2,1],[0,2],[1,2],[0,3]]
number=0

def inlaw(x,y):
    if x>=0 and y>=0 and x<n and y<m:
        return True
    else:
        return False

def DFS(x,y):
    global number,max_
    if x==n-1 and y==m-1:
        if number>max_:
            max_=number
    else:
        for way in ways:
            n_x=x+way[0]
            n_y=y+way[1]
            if inlaw(n_x,n_y):
                number+=maps[n_x][n_y]
                DFS(n_x,n_y)
                number-=maps[n_x][n_y]
            
        

(n,m)=map(int,input().split())
maps=[]
for i in range(n):
    temp=list(map(int,input().split()))
    maps.append(temp)

for way in ways:
    number+=maps[0][0]
    DFS(0,0)
    number-=maps[0][0]

print(max_)
