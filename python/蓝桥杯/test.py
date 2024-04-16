#求x^a

def qpow(x,a):
    result=1
    while a!=0:
        if (a&1)==1:
            result=result*x
        a>>=1
        x=x*x
    return result

print(qpow(2,10))
