s=list(input())

times=pow(2,64)

while times>0:
    flag=False
    remov=[]
    
    remov=[0,0,0]
    s_temp=[]
    for i in range(1,len(s)-1):
        
        if s[i]==s[i-1]:
            flag=True
        if s[i-1]==s[i] and s[i]!=s[i+1]:
            remov[1]=1
            remov[2]=1
        if s[i]!=s[i-1] and s[i]==s[i+1]:
            remov[0]=1
            remov[1]=1
        if remov[0]==0:
            s_temp.append(s[i-1])
        remov.pop(0)
        remov.append(0)
    if len(s)>=2 and remov[0]==0:
        s_temp.append(s[-2])
    if len(s)>=1 and remov[1]==0:
        s_temp.append(s[-1])

    s=s_temp.copy()
            
    if flag==False: #不在有连续字符
        break

if len(s)==0:
    print("EMPTY")
else:
    print("".join(s))
        

"""
sdfhhhhcvhhxcxnnnnshh
sdFHhhHCVHHXcXNnnNSHh
sdhhcnnh
sDHHCNNH
s
"""
