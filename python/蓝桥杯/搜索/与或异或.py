arr=[[1,0,1,0,1],[],[],[],[]]
f=1
count=0


def app(x):
    global arr
    for i in range(5):
        if len(arr[i])==5-i:
            continue
        else:
            arr[i].append(x)
            break

def subb():
    global arr
    for i in range(4,0,-1):
        if len(arr[i])==0:
            continue
        else:
            arr[i].pop()
            break

def caculate(op,x,y):
    if op==0:
        return x|y
    elif op==1:
        return x^y
    elif op==2:
        return x&y
    

def DFS(i,j):
    global count,f
    if len(arr[-1])==1:
        if arr[-1][0]==1:
            count+=1
    else:
        if i==1 and j==3 or i==2 and j==2 or i==3 and j==1:
            n_i=i+1
            n_j=0
            f+=1
        else:
            n_i=i
            n_j=j+1
            
        for p in range(3):
            n_res=caculate(p,arr[n_i-1][n_j],arr[n_i-1][n_j+1])
            app(n_res)
            DFS(n_i,n_j)
            subb()
            
            


for i in range(3):
    res=caculate(i,arr[0][0],arr[0][1])
    app(res)
    DFS(1,0)
    subb()

print(count)
