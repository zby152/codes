T=int(input())
for _ in range(T):
    A=list(map(int,input().split()))
    A.sort()
    dist_A=set(A)
    
    length=len(dist_A)
    if length>=3:
        print(2)
    elif length==1:
        print(0)
    elif A[1]==A[2]:
        print(1)
    else:
        print(2)
