
words = list(input().split())
ans = ""

for word in words:
    d=0
    res=""
    if not word[0].isdigit():
        res = word[0].upper()
        d=1

    flag = 0 # 1表示进入数字
    for i in range(d,len(word)):
        if word[i].isdigit() and flag==0 :
            res = res + '_'
            flag = 1
            if i==0:
                res=""
        elif not word[i].isdigit() and flag==1:
            res=res+'_'
            flag=0
        res=res+word[i]
    ans=ans+res+" "
print(ans)