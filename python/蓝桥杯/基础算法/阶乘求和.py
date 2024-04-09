
def get_(x):
    res=1
    for ii in range(1,x+1):
        res=res*ii
    return res
ans=0

for i in range(1,41):
    num=get_(i)
    ans=ans+num%1000000000
    # print("{:0100}".format(num))

ans_str=str(ans)[-9:]
print(ans_str)

# print(420940313)
