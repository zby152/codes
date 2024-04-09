import datetime
N=""

def judge1(n_time):

    n_y=str(n_time.year)
    
    n_m=str(n_time.month)
    if len(n_m)==1:
        n_m="0"+n_m
        
    n_d=str(n_time.day)
    if len(n_d)==1:
        n_d="0"+n_d
        
    n=""
    n=n+n_y+n_m+n_d
    n_r=n[::-1]
    if n_r==n:
        print(n)
        return 1
    else:
        return 0

def judge2(n_time):
    n_y=str(n_time.year)
    n_m=str(n_time.month)
    if len(n_m)==1:
        n_m="0"+n_m
        
    n_d=str(n_time.day)
    if len(n_d)==1:
        n_d="0"+n_d
        
    n=""
    n=n+n_y+n_m+n_d
    A=n[0]
    B=n[1]
    n_f=A+B+A+B+B+A+B+A
    if n_f==n:
        print(n)
        return 1
    else:
        return 0

N=input()
y=int(N[:4])
m=int(N[4:6])
d=int(N[6:])

now=datetime.date(y,m,d)

i=1
flag1=0
flag2=0
while True:
    next_time=now+datetime.timedelta(days=i)
    i+=1
    if flag1==0:
        flag1=judge1(next_time)
    if flag2==0:
        flag2=judge2(next_time)
    if flag1==1 and flag2==1:
        break
