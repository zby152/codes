(n,k)=map(int,input().split())
D=[]
for _ in range(n):
    word=input()
    D.append(word)
D.sort(key=lambda x: len(x), reverse=True)

for _ in range(k):
    code=input()
    i=0
    flag=1
    while flag==1 and i<len(code):
        temp=i
        for d in D:
            if d[0]==code[i] and d==code[i:i+len(d)]:
                i+=len(d)
                break
        if temp==i:
            flag=0
    print(i)
