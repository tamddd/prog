#アルゴ式 友達の友達
from collections import defaultdict
n, m, x= map(int, input().split())

if m == 0:
    exit()

d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
fri = set()
for i in d[x]:
    for j in d[i]:
        if j not in d[x] and j != x:
            fri.add(j)

print(len(fri))
