#求最小公倍和最大公因数，除法过程中如果浮点数溢出会产生误差，
# 如果确定是整除就要用整除符号

import math

def get_mi(a,b):
    return a*b//math.gcd(a,b)

N=int(input())
n=[i for i in range(2,N+1)]
while len(n)>=2:
    a=n.pop(0)
    b=n.pop(0)
    c=get_mi(a,b)
    if c not in n:
        n.append(c)

print(n[0])
