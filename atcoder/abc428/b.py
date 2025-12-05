from collections import Counter
n, k = map(int, input().split())
s = input()
c = Counter(s[i:i+k] for i in range(n-k+1))
max_val = max(c.values())
ans = []
for i in c.items():
  if i[1] == max_val:
    ans.append(i[0])
ans.sort()

print(max_val)
for i in ans:
  print(i)
