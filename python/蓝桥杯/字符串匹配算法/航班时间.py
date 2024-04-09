# 时间模块
import datetime

def get_time(second):
    h=0
    m=0

    while second>=60:
        m+=1
        second-=60
        if m>=60:
            h+=1
            m=0
    s=second
    return h,m,s


T = int(input())
for _ in range(T):
    times = ["", "", "", ""]
    l = list(input().split())
    times[0], times[1] = l[0], l[1]
    x1, x2 = 0, 0
    if len(l) == 3:
        x1 = int(l[2][2])

    l = input().split()
    times[2], times[3] = l[0], l[1]
    if len(l) == 3:
        x2 = int(l[2][2])

    Times = []
    for i in range(4):
        t = times[i]
        d = 1
        h = int(t[:2])
        m = int(t[3:5])
        s = int(t[6:])
        if i == 1:
            d = x1 + 1
        if i == 3:
            d = x2 + 1

        Times.append(datetime.datetime(2000, 1, d, h, m, s))
    t1 = Times[1] - Times[0]
    t2 = Times[3] - Times[2]
    se=(t1.seconds+t2.seconds+24*60*60*t1.days+24*60*60*t2.days)//2
    h,m,s=get_time(se)
    ans=datetime.time(h,m,s)
    print(ans)
