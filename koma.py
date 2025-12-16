#アルゴ式 dp
n = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i+1 < n:
            dp[i+1][j] += dp[i][j]
        if j+1 < n:
            dp[i][j+1] += dp[i][j]

print(dp[n-1][n-1])
