# 辗转相除约分分数,找最大公因数

def get_small(l):
    a=l[0]
    b=l[1]
    x,y=a,b
    while b>0:
        a,b=b,a%b
    x=int(x/a)
    y=int(y/a)
    return [x,y]

N=int(input())
x=map(int,input().split())
x=sorted(x)

q=[]
for i in range(N):
    for j in range(i+1,N):
        if x[j]==x[i] :
            continue
        temp=[x[j],x[i]]
        temp_=get_small(temp)
        if temp_ not in q:
            q.append(temp_)

min_index=0
min_t=q[0][0]/q[0][1]
for i in range(len(q)):
    t=q[i][0]/q[i][1]
    if t<min_t:
        min_t=t
        min_index=i

print(str(q[min_index][0])+"/"+str(q[min_index][1]))
