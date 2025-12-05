from collections import Counter
n, k = map(int, input().split())
s = input()
ans = sorted(Counter([s[i:i+k] for i in range(n-k+1)]).items(), key=lambda x : x[1])[-1]
print(ans[1])
print(ans[0])
