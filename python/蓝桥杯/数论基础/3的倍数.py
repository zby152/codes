a=int(input())
b=int(input())
c=int(input())

res1=(a+b)%3
res2=(a+c)%3
res3=(b+c)%3

if res1==0 or res2==0 or res3==0:
    print("yes")
else:
    print("no")
