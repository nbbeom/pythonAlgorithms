# 2계단 혹은 3계단 만 가능


# 2계단을 만가능..
n = int(input())

dp = [0] * (1001)
#초기 조건
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

#점화식 dp[i] = dp[i-2] +dp[i-3]

for i in range(4,n+1):
    dp[i] = (dp[i-2]+dp[i-3])% 10007

print(dp[n])