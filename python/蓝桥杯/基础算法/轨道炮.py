N=int(input())
X=[]
Y=[]
Vx=[]
Vy=[]
for _ in range(N):
    xi,yi,vi,di=input().split()
    X.append(int(xi))
    Y.append(int(yi))
    vi=int(vi)
    if di=='L':
        Vx.append(-vi)
        Vy.append(0)
    if di=='R':
        Vx.append(vi)
        Vy.append(0)
    if di=='U':
        Vx.append(0)
        Vy.append(vi)
    if di=='D':
        Vx.append(0)
        Vy.append(-vi)

def cal(ps,vs):
    res=1
    for i in range(N):
        p1=ps[i]
        v1=vs[i]
        same=1
        numbers={}
        for j in range(N):
            if i==j: continue
            p2=ps[j]
            v2=vs[j]
            dx=p2-p1
            dv=v1-v2
            if dv==0:
                if dx==0:
                    same+=1
                    res=max(res,same)
            else:
                t=dx//dv
                if dx%dv!=0 or t<0: continue
                else:
                    numbers[t]=numbers.get(t,0)+1
                    res=max(res,same+numbers[t])
    return res
        

row=cal(X,Vx) #纵向开炮只需要算横向的方向能不能放一起
col=cal(Y,Vy) #横向开炮
ans=max(row,col)
print(ans)

"""
5
0 0 1 U
1 1 2 U
2 2 3 U
3 3 4 U
4 4 5 U
"""

