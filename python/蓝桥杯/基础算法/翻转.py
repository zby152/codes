d = int(input())
for _ in range(d):
    count=0
    t = list(input())
    s = list(input())
    n=len(s)
    for i in range(1,n-1):
        if s[i]==t[i]:
            continue
        elif s[i]!=s[i-1] and s[i]!=s[i+1]:
            s[i]=s[i-1]
            count+=1
    if s==t:
        print(count)
    else:
        print(-1)


