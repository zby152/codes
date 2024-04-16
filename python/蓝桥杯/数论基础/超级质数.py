def is_zhi(n):
    for i in range(2,n):
        if n%i==0:
            return False #是质数
    return True #不是质数

def find(x):
    length=len(x)
    for i in range(length):
        for j in range(i+1,length+1):
            num=x[i:j]
            if not is_zhi(int(num)):
                return False # 不是质数
    return True 

max_res=0
for i in range(1,1000000):
    num=str(i)
    if '8' in num or '9' in num or '4' in num or '6' in num or '1' in num:
        continue
    if find(num):
        print(num)
        max_res=num
print(max_res)



