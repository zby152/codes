import math
n=int(input())
A=list(map(int,input().split()))

A.sort()

test=A[0]+1
cnt=0
res=A[0]

while(True):
    for ai in A:
        if ai==test-1:
            cnt+=1
        
    if cnt%test==0:
        res=test
        cnt=cnt/test
        test+=1
    else:
        break

print(res)
