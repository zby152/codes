number=2022
part=10

dp=[[0]*(part+1) for _ in range(number+1)]

for i in range(1,number+1):
    dp[i][1]=1
dp[0][0]=1

for i in range(1,number+1):
    for j in range(1,part+1):
        if i>j:
            dp[i][j]=dp[i-j][j]+dp[i-j][j-1]

print(dp[number][part])
    
