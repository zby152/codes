# 贪心算法，注意审题，并不是事件发生的顺序确定

n=0
A=[]
B=[]
C=[]

def judge(a,b,c):
    w=0
    cont=[]
    for i in range(n):
        cont.append(a[i]-b[i]-c[i])
    cont.sort(reverse=True)
    for i in range(n):
        w+=cont[i]
        if w<=0:
            return i
    return n

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

res=max(judge(A,B,C),judge(B,C,A),judge(C,A,B))
if res==0:
    print(-1)
else:
    print(res)
