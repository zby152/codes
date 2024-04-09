# 对总时间进行排序然后贪心

def fun(x):
    return x[0]+x[1]

n=int(input())
times=[]
for _ in range(n):
    s,a,e=map(int,input().split())
    times.append([s+a,e])

t_sorted=sorted(times,key=fun)

t=t_sorted[0][0]
res=[t]
for i in range(1,n):
    t=t+t_sorted[i-1][1]+t_sorted[i][0]
    res.append(t)
ans=sum(res)
print(ans)