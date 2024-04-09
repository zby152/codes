import os
import sys

# 请在此输入您的代码
# 118 机器人塔

# 实际上就是A=0，B=1，异或运算

# 总人数s=(n**2+n)/2，每层人数是个等差数列

# 求出来层数，从第一层开始，只要第一个人定了，后面的都就定了，算数就行了。算到人不够还组不好就不行。刚好人数也够的就可以，判断2的n次方下就行了
from itertools import product

na,nb=map(int,input().split())
n=int(((1+8*(na+nb))**0.5-1)/2 )# 层数
lp=list(product([0,1,2],repeat=n)) # 所有可能组合
result=0

for p in lp:
    print(p)
"""
# 循环每种组合
for p in lp:
    nab=[na,nb]
    # 逐层减掉人数
    ls=[p[0]] # 上一层的情况
    nab[p[0]]-=1
    lx=[] # 在算的这一层的情况
    for j in range(1,n):
        lx.append(p[j]) # 先把组合定下来的左边的数处理掉
        nab[p[j]]-=1
        for k in ls: # 循环处理这一层剩下的
            lx.append(k ^ lx[-1])
            nab[lx[-1]]-=1
        ls=lx
        lx=[] # 更新一下这两层的状态
    if min(nab)>=0:
        result+=1

print(result)
"""
