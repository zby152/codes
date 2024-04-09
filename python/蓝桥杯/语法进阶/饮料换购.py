n=int(input())

result=0
m=0

while n>0:
    result+=n
    m+=n
    n=m//3
    m=m%3

print(result)
