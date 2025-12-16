#アルゴ式 ヒストグラム

from collections import Counter
n = int(input())
c = Counter(i//10 for i in list(map(int, input().split())))

for i in range(10):
    print(c[i])

"""
from collections import Counter
n = int(input())
d = Counter(list(map(lambda x : int(x) // 10, input().split())))

for i in range(0, 10):
    print(d[i])
"""
