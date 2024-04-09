letters=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
numbers=['0','1','2','3','4','5','6','7','8','9']

ans=0
def DFS(i):
    global p,ans
    if i==6:
        ans+=1
        return
    else:
        if i<=2:
            for l in letters:
                if len(p)>=2:
                    if l==p[-1] and l==p[-2]:
                        continue
                p.append(l)
                DFS(i+1)
                p.pop()
        else:
            for l in numbers:
                if len(p)>=2:
                    if l==p[-1] and l==p[-2]:
                        continue
                p.append(l)
                DFS(i+1)
                p.pop()

p=[]
DFS(0)
print(ans)
