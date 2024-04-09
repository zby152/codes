x,y=map(int,input().split())
ans=0

if x>=0 and y>=0:
    if x<=y:
        ans=(y*2)**2-(y-x)
    if x>y:
        ans=(x*2)**2+(x-y)
elif x>=0 and y<0:
    if x>abs(y):
        ans=(x*2)**2+(x-y)
    if x<=abs(y):
        ans=(abs(y)*2+1)**2-1-(x-y)
elif x<0 and y<0:
    if x<y:
        ans=(abs(x)*2-1)**2+(y-x-1)
    if x>=y:
        ans=(abs(y)*2)**2-1-(x-y)
elif x<0 and y>=0:
    if abs(x)<y:
        ans = (abs(y) * 2 ) ** 2 - (y + abs(x))
    if abs(x)>=y:
        ans = (abs(x) * 2-1) ** 2 + (y + abs(x)-1)
print(ans)