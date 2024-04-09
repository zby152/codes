# 数据量超过10**9的时候单次遍历必定会超时，应该考虑能一下算一大部分的算法
a,b,n=map(int,input().split())

while n>1000: #每1000位计算一次，优化时间，
    a=a*(10**1000)
    n-=1000
    a=a%b #例如a*100之后小数位第一位就是之前的第三位，加了2

a_=a%b # a_代表每一轮次的被除数
res=[]
cnt=0 # 已经找到的位数

while True:
    a_=a_*10
    x=a_//b
    res.append(x)
    cnt+=1
    a_=a_-x*b
    if cnt==n+2:
        break
    if a_==0:
        if cnt<n:
            flag=3
        elif cnt>=n and cnt<n+2:
            flag=n+2-cnt
        for i in range(flag):
            res.append(0)
        break


for i in range(-3,0,1):
    print(res[i],end="")