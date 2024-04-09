# 动态规划 分成子问题
# 考虑dp[n]和dp[n-1]的问题，du[n]就相当于先淘汰一个再从4开始也就是说多一个人就多开始一个k
# 也就是说上一个问题加上一个k的编号是这一个问题的编号

n,k=map(int,input().split())
dp=0
for i in range(2,n+1):
  dp=(dp+k)%i
print(dp+1)