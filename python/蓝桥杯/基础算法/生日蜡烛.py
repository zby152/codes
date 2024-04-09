res=0

for k in range(26,30):
    number=0
    for n in range(20):
        number=number+k+n
        if number==236:
            res=k

print(res)
