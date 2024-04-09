n=int(input())
a=list(map(int,input().split()))

maxa=a[1]-a[0]
for i in range(n-1):
    if a[i+1]-a[i]>maxa:
        maxa=a[i+1]-a[i]

print(maxa)
