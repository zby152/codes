n=int(input())
a=list(map(int,input().split()))

max_dis=0
for i in range(n):
    for j in range(n):
        dis=abs(i-j)+abs(a[i]-a[j])
        if dis>max_dis:
            max_dis=dis

print(max_dis)
