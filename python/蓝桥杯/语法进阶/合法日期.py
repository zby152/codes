import datetime

m=int(input())
d=int(input())

try:
    temp=datetime.date(2021,m,d)
    print("yes")
except:
    print("no")

