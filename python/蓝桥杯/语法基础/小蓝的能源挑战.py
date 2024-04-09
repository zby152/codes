T=int(input())
for _ in range(T):
    (x,y)=map(int,input().split())
    if x*5>=y:
        print("YES")
    else:
        print("NO")
