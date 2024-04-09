(D,C)=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

unbuy=0
buy=0

A_all=0
for a in A:
    A_all+=a

B_all=0
for b in B:
    B_all+=b

unbuy=A_all+B_all+2*D

buy=A_all+B_all+C

if A_all<=150:
    buy+=D
if B_all<=150:
    buy+=D

if buy<unbuy:
    print("YES")
else:
    print("NO")
