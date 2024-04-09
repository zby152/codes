# 不能太过于盲目的用广搜，能用贪心解决就用贪心解决

start = list(input())
end = list(input())
n = len(start)
i=0
res=0
while i<n-1:
    if start[i]!=end[i]:
        res+=1
        if start[i+1]=="o":
            start[i+1]="*"
        else:
            start[i+1]="o"
    i+=1
print(res)