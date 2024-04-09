T=int(input())

for _ in range(T):
    (x,s,y)=input().split()
    x=int(x)
    y=int(y)
    if s=='MB':
        x=1024*1024*x
    elif s=='KB':
        x=1024*x
    count=x//y
    print(count)
