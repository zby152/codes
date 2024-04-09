n=int(input())
a=list(map(int,input().split()))

count=1
max_count=0
last_a=a[0]

for i in a:
    if last_a<i:
        count+=1
    else:
        if max_count<count:
            max_count=count
        count=1
    last_a=i

print(max_count)
