"""
n1=12345678
n2=98765432
result=0

for i in range(n1,n2+1):
    flag=0
    for ch in str(i):
        if flag==0 and ch=="2":
            flag=1
        if flag==1 and ch=="0":
            flag=2
        if flag==2 and ch=="2":
            flag=3
        if flag==3 and ch=="3":
            flag=4
            break
    if flag==4:
        result+=1

print(result)
"""
      
print(98765433-12345678-460725)
