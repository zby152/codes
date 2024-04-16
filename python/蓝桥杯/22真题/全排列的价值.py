N=1000000
dp=[0]*N
dp[1]=0
dp[2]=1
dp[3]=9

n=int(input())
mem1=[0]*N
mem2=[0]*N

def cal(x):
    if mem1[x]:
      return mem1[x],mem2[x]
    sum1=0
    sum2=1
    for i in range(1,x+1):
        sum1+=i
        sum2*=i
    mem1[x]=sum1
    mem2[x]=sum2
    return sum1,sum2

        

for i in range(4,n+1):
    x1,x2=cal(i-1)
    dp[i]=i*dp[i-1]+x1*x2

print(dp[n]%998244353)
