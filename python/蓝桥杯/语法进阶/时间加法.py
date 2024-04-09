a=int(input())
b=int(input())
t=int(input())

time=a*60+b
time_2=(time+t)%1440

hour=time_2//60
minute=time_2%60

print(hour)
print(minute)
