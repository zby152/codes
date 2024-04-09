n=int(input())

a=list(map(int,input().split()))

result=[0 for _ in range(len(a))]

for i in range(n):
    for j in range(i+1,n):
        if a[i]<a[j] and result[j]==0:
            for k in range(j+1,n):
                if a[j]<a[k]:
                    result[j]=1

count=0
for x in result:
    if x==1:
        count+=1

print(count)
