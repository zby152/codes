N=int(input())
A_=list(map(int,input().split()))
B_=list(map(int,input().split()))
C_=list(map(int,input().split()))

A=sorted(A_)
B=sorted(B_)
C=sorted(C_)

res=0
i=N-1
j=0
k=0
while i>=0 and j<N and k<N:
    if A[i]<B[j] and B[j]<C[k]:
        res+=1
        res+=N-1-k
        k=N-1
        
    if k==N-1:
        k=0
        j=j+1
        if j==N:
            j=0
            i=i-1
    else:  
        k+=1

print(res)
