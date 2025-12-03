#アルゴ式 双六
n, m = map(int, input().split())
d = list(map(int, input().split()))
dp = [False for _ in range(n+1)]
dp[0] = True

for i in d:
    for j in range(n+1):
        if dp[j] and i+j <= n:
            dp[i+j] = True

print("Yes" if dp[n] else "No")
