n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(n):
    for j in range(n):
        if j+1 < n:
            dp[j+1] += dp[j]

print(dp[n-1])
