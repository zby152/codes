import datetime

start=datetime.datetime(1900,1,1)
end=datetime.datetime(9999,12,31)

add_one=datetime.timedelta(days=1)

ans=0
while start<end:
    year1=start.year
    month1=start.month
    day1=start.day

    sum_l=0
    for i in str(year1):
        sum_l+=int(i)

    sum_r=0
    for i in str(month1):
        sum_r+=int(i)
    for i in str(day1):
        sum_r+=int(i)

    if sum_l==sum_r:
        ans+=1

    start=start+add_one

print(ans)
