n=int(input())

i=2
ans=0

while i**2<n:
    if n%i==0:
        ans+=1
        while n%i==0:
            n=n//i
    i+=1
if n>1:
    ans+=1

print(ans)
