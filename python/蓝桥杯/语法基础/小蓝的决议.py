T=int(input())
for _ in range(T):
    (n,x)=map(int,input().split())
    if x*2>=n:
        print("YES")
    else:
        print("NO")
