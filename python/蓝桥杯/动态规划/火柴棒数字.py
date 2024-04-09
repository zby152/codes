n=300

def dfs(i,x):
    if i>n:
        return 0
    else:
        num0=dfs(i+6)*10+x
        num1=dfs(i+2)*10+x
        num2=dfs(i+5)*10+x
        num3=dfs(i+5)*10+x
        num4=dfs(i+4)*10+x
        num5=dfs(i+5)*10+x
        num6=dfs(i+6)*10+x
        num7=dfs(i+3)*10+x
        num8=dfs(i+7)*10+x
        num9=dfs(i+6)*10+x
        return max(num0,num1,num2,num3,num4,num5,num6,num7,num8,num9)


ans=dfs(0,0)
