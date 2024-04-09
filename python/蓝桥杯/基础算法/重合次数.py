import datetime

start_time=datetime.time(hour=6,minute=13,second=22)
end_time=datetime.time(hour=14,minute=36,second=20)

one_second=datetime.timedelta(hours=0,minutes=0,seconds=1)

ans=0
while start_time!=end_time:
    start_time = (datetime.datetime.combine(datetime.date.today(), start_time) + one_second).time()
    if start_time.minute==start_time.second and start_time.minute!=59:
        ans+=1

print(ans)