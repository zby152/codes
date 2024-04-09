def is_right(y):
    global r,g,b
    
    if r<0 or g<0 or b<0:
        return False
    else:
        return True

def find(y):
    t=[1]
    for i in range(1,len(y)):
        if y[i]==y[i-1]:
            t[-1]+=1
        else:
            t.append(1)
    for i in range(1,len(t)):
        if t[i-1]>=t[i]:
            return False
    return True

def cut(y):
    t=[1]
    for i in range(1,len(y)):
        if y[i]==y[i-1]:
            t[-1]+=1
        else:
            t.append(1)
    for i in range(1,len(t)-1):
        if t[i-1]>=t[i]:
            return False
    return True
        

def DFS(n):
    global count,number_all,r,g,b,x
    if n==number_all and find(x):
        count+=1
    else:
        r-=1
        x.append(1)
        if is_right(x) and cut(x):
            DFS(n+1)
        r+=1
        x.pop()

        g-=1
        x.append(2)
        if is_right(x) and cut(x):
            DFS(n+1)
        g+=1
        x.pop()

        b-=1
        x.append(3)
        if is_right(x) and cut(x):
            DFS(n+1)
        b+=1
        x.pop()
        
            

(R,G,B)=map(int,input().split())
number_all=R+G+B
count=0

r=R
g=G
b=B
x=[1]
r-=1
DFS(1)

r=R
g=G
b=B
x=[2]
g-=1
DFS(1)

r=R
g=G
b=B
x=[3]
b-=1
DFS(1)

print(count)











