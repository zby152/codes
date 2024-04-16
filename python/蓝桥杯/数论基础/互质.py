import math

ans=0
for i in range(1,2021):
    if math.gcd(i,1018)==1:
        ans+=1
print(ans)
