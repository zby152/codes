"""
import datetime

def judge(y,m,d):
    y_s=str(y)
    m_s=str(m)
    d_s=str(d)
    
    sum_y=0
    sum_md=0
    
    for i in y_s:
        sum_y+=int(i)

    for j in m_s:
        sum_md+=int(j)

    for k in d_s:
        sum_md+=int(k)

    if sum_y==sum_md:
        return True
    else:
        return False
        

count=0

for year in range(1900,10000):
    for month in range(1,13):
        for day in range(1,32):
            try:
                temp=datetime.date(year,month,day)
                if judge(year,month,day):
                    count+=1
            except:
                continue

print(count)
"""
print(70910)
