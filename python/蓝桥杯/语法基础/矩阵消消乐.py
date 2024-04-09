def judje(num):
    times2=[1,2,4,8,16,32,64,128,256,512,1024]
    if num in times2:
        return True
    else:
        return False


N=int(input())
maps=[]

for _ in range(N):
    temp=list(map(int,input().split()))
    maps.append(temp)

rows=[]
cols=[]

for i in range(N):
    for j in range(N):
        if judje(maps[i][j]):
            rows.append(i)
            cols.append(j)

for row in rows:
    for y in range(N):
        maps[row][y]=1

for col in cols:
    for x in range(N):
        maps[x][col]=1   

for i in range(N):
    for j in range(N):
        print(maps[i][j],end=' ')
    print()

