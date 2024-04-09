# 尽量不要使用二位列表，时间开销太大

import collections
import sys

ops=[1,-1,2,-2,3,-3]

def jump(z,op):
    x=z.copy()
    i=x.index("*")
    y=i+op
    
    if y>=0 and y<len(x):
        x[i],x[y]=x[y],x[i]
        return x
    else:
        return None
    

start=list(input())
end=list(input())
invited=set()

Q=collections.deque()

Q.append([start,0])
invited.add("".join(start))

while len(Q)!=0:
    temp,step=Q.popleft()
    
    for op in ops:
        n_temp=jump(temp,op)
        n_step=step+1
        if n_temp!=None:
            if n_temp==end:
                print(n_step)
                sys.exit(0)
            n_temp_str="".join(n_temp)
            if n_temp_str not in invited:
                Q.append([n_temp,n_step])
                invited.add(n_temp_str)
        
