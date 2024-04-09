MAX=1000000007
N=int(input())

ans=0
for i in range(1,N):
    ans+=i*((N-i)**2)

print(ans%MAX)
