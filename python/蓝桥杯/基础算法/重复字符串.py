# asc码的典型值

k=int(input())
s=input()
n=len(s)//k

res=[{chr(i):0 for i in range(97,123)} for _ in range(n)]
if len(s)%k!=0:
    print(-1)
else:
    group=[]
    for i in range(k):
        temp=s[i*n:(i+1)*n]
        group.append(temp)
        for j in range(n):
            res[j][temp[j]]+=1
    ans=0
    for i in range(n):
        temp=res[i]
        max_ch=max(temp.values())
        ans=ans+k-max_ch
    print(ans)


