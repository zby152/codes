string=input()
res={}

def find_max(dic):
    max_key=[]
    lis=list(dic.values())
    max_value=max(lis)
    for i in range(len(lis)):
        if lis[i]==max_value:
            max_key.append(list(dic.keys())[i])

    return max_key

for ch in string:
    if res.get(ch):
        res[ch]+=1
    else:
        res[ch]=1

max_key = find_max(res)
max_key.sort()

print(max_key[0])
print(res[max_key[0]])
