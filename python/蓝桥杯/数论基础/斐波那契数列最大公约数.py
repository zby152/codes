import math

f=[0]*2030
f[1]=1
f[2]=1

for i in range(3,2030):
    f[i]=f[i-1]+f[i-2]

a=f[520]
b=f[2020]

res=math.gcd(a,b)
print(res)
