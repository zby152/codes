(k,N)=map(int,input().split())

result=[]

for i in range(13):
    temp=[]
    times=k**i
    temp.append(times)
    for x in result:
        temp.append(times+x)
    result=result+temp

# print(result)
print(result[N-1])
