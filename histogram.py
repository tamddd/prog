#アルゴ式 ヒストグラム

from collections import Counter
n = int(input())
c = Counter(i//10 for i in list(map(int, input().split())))

for i in range(10):
    print(c[i])
