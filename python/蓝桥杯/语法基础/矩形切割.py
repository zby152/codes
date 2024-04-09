a=2019
b=324

count=1

while a!=b:
    max_ab=max(a,b)
    min_ab=min(a,b)
    a=max_ab-min_ab
    b=min_ab
    count+=1

print(count)
