n=int(input())
for _ in range(0,n):
    (x,y)=map(int,input().split())
    if x<y:
        print(0)
    else:
        print(x-y)
