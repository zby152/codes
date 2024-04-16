

dic={}
for i in range(1,81):
    if i<=10:
        dic[i]=1
    elif i<=20:
        dic[i]=2
    elif i%10==0:
        dic[i]=2
    else:
        dic[i]=3

res=[]
for num in range(1,21):
    monse=num
    eye=2*num
    legs=4*num

    x1=dic[num]+3
    x2=dic[monse]+2
    x3=dic[eye]+3
    x4=dic[legs]+2

    res.append(x1+x2+x3+x4)

print(sum(res))
    
