# 理解题意，字符串之间的字典序


(n,x)=map(int,input().split())
s=list(input())
s.sort()

if s[0]!=s[x-1]:
    print(s[x-1])
else:
    if s[x]==s[-1]:
        print(s[x-1],end="")
        for ch in range(x,n,x):
            print(s[x],end="")
    else:
        print("".join(s[x-1:]))

