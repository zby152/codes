nums=[99,22,51,63,72,61,20,88,40,21,63,30,11,18,99,12,93,16,7,53,64,9,28,84,34,96,52,82,51,77]

count=0
for i in range(30):
    for j in range(30):
        if i!=j:
            result=nums[i]*nums[j]
            if result>=2022:
                count+=1

count/=2
print(int(count))
