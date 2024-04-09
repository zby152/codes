# 调用product库进行限制总长度的
from itertools import product

M=0
N=0

def one(last_floor,count_a,count_b):
    """x是上一层的排列情况"""
    now_floor=[]
    if len(last_floor)==2:
        if last_floor[0]==last_floor[1] and count_a==1:
            return 1
        elif last_floor[0]!=last_floor[1] and count_b==1:
            return 1
        else:
            return 0
    else:
        for i in range(len(last_floor)-1):
            if last_floor[i]==last_floor[i+1]:
                count_a-=1
                now_floor.append("A")
            else:
                count_b-=1
                now_floor.append("B")
            if count_a<0 or count_b<0:
                return 0
        return one(now_floor,count_a,count_b)
    
        
(M,N)=map(int,input().split())

n=0
for i in range(500):
    if i*(i+1)==2*(M+N):
        n=i
        break


result=0

A=[]

first_floor=[]
A=list(product(["A","B"],repeat=n))

for start in A:
    i=0
    j=0
    for s in start:
        if s=="A":
            i+=1
        else:
            j+=1
    result+=one(start,M-i,N-j)


print(result)
