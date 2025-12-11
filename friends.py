#アルゴ式 人気者の友達
from collections import defaultdict
n, m = map(int, input().split())

if m == 0:
    exit()

d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

ans = sorted(d.items(), key=lambda x : (-len(x[1]), x[0]))[0][1]
print(*sorted(ans))
