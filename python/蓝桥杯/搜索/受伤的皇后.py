
count=0

def is_right(x,y):
    if x>=4 or y>=4:
        return False
        
    invalide[x][y]=1
    for i in range(n):
        cnt=0
        for j in range(n):
            if invalide[i][j]==1:
                cnt+=1
            if cnt>1:
                invalide[x][y]=0
                return False
        
    for j in range(n):
        cnt=0
        for i in range(n):
            if invalide[i][j]==1:
                cnt+=1
            if cnt>1:
                invalide[x][y]=0
                return False

    dig=[]
    for i in range(n):
        for j in range(n):
            if invalide[i][j]==1:
                dig.append([i,j])

    for i in range(len(dig)):
        for j in range(i+1,len(dig)):
            c_x=abs(dig[j][0]-dig[i][0])
            c_y=abs(dig[j][1]-dig[i][1])
            if c_x==c_y and c_x<3:
                invalide[x][y]=0
                return False
    
    invalide[x][y]=0
    return True

def DFS(i,x,y):
    global count
    if i==4:
        count+=1
    else:
        for k in range(n):
            if is_right(x+1,k):
                invalide[x+1][k]=1
                DFS(i+1,x+1,k)
                invalide[x+1][k]=0

n=int(input())
invalide=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    invalide[0][i]=1
    DFS(1,0,i)
    invalide[0][i]=0

print(count)
