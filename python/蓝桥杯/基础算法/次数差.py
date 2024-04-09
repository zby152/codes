string=input()

times=[0 for _ in range(26)]

for ch in string:
    ch_num=ord(ch)-97
    times[ch_num]+=1


times=sorted(times)
max_=times[-1]
for i in times:
    if i!=0:
        min_=i
        break

print(max_-min_)
