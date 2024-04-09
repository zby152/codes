# 正则表达式相关的概念

def find_big(x):
    return len(x)

def short(s):
    s_part=[]
    temp=""
    for ch in s:
        if ch=="|":
            s_part.append(temp)
            temp=""
        else:
            temp=temp+ch
    if temp!="":
        s_part.append(temp)

    s_sort=sorted(s_part,key=find_big)
    
    return s_sort[-1]
            

def end(s):
    for ch in s:
        if ch=="(" or ch=="|":
            return False
    return True

def caculate(s):
    temp=""
    k=0
    for i in range(len(s)):
        if s[i]=="(":
            temp=""
            k=i
        elif s[i]==")":
            res=short(temp)
            s=s[:k]+res+s[i+1:]
            temp=""
            break
        else:
            temp=temp+s[i]
    if "|" in temp:
        s=short(temp)
    return s
            

string=input()

while end(string)==0:
    string=caculate(string)

print(len(string))
