"""
ans=0

def DFS(m,n,k):
    global ans
    
    if k==7:
        if m+n>=2 and m+n<=5:
            ans+=1
            
        return

    for i in range(2,6):
        for j in range(min(m,i)+1):
            l=i-j
            if l<=n:
                DFS(m-j,n-l,k+1)

a=9
b=16

DFS(a,b,1)
print(ans)
"""
print("5067671")
