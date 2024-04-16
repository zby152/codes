n=int(input())
a=[0]*(n+2)
a[1:n+1]=list(map(int,input().split()))
m=int(input())

cnt=[0]*(n+2)
diff=[0]*(n+2)

front_sum=0

for _ in range(m):
    L,R=map(int,input().split())
    diff[L]+=1
    diff[R+1]-=1

for i in range(1,n+1):
    cnt[i]=cnt[i-1]+diff[i]

for i in range(1,n+1):
    front_sum+=cnt[i]*a[i]
        
cnt.pop(0)
cnt=sorted(cnt,reverse=True)
c=sorted(a,reverse=True)

after_sum=0
for i in range(n):
    after_sum+=c[i]*cnt[i]


print(after_sum-front_sum)

"""
5
1 2 3 4 5
2
1 3
2 5
"""
