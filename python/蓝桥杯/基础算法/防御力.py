# 难理解的一道贪心，涉及到数学知识
import os
import sys
n1,n2=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=list(input())
#输入
for i in l:
  if i=='0':
    a=l1.index(min(l1))
    print(f'A{a+1}')
    l1[a]=2**31
  else:
    b=l2.index(max(l2))
    print(f'B{b+1}')
    l2[b]=-1
#根据贪心思想可知：A从小到大，B从大到小。注意格式化输出和序号
print('E')