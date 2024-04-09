N=int(input())

ids=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    ids.extend(temp)

ids.sort()

i=1
m=0
n=0

while True:
    if ids[i-1]+1==ids[i]:
        i+=1
        continue
    else:
        if ids[i]==ids[i-1]:
            n=ids[i]
            i+=1
        else:
            m=ids[i]-1
            i+=1
        if n!=0 and m!=0:
            break

print(str(m)+" "+str(n))
    
