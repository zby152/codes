def judge(num):
    num_s=str(num)
    for ch in num_s:
        if ch=="2":
            return False
    return True

n=int(input())
res=0

for i in range(1,n+1):
    if judge(i):
        res+=1
print(res)