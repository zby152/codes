n=int(input())

numbers=["2","0","1","9"]

sum=0
for i in range(n+1):
    i_str=str(i)
    flag=0
    for ch in i_str:
        if ch in numbers:
            flag=1
    if flag==1:
        sum+=i

print(sum)
