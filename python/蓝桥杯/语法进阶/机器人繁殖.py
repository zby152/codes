def get_a(n_):
    sum=0
    for i in range(n_+1):
        sum+=2**i
    return sum

        
def get_b(n_):
    sum=0
    for i in range(1,n_+1):
        sum+=2**i-1
    return sum


(n,s)=map(int,input().split())
a=get_a(n)
b=get_b(n)
x=int((s+b)/a)

print(x)
