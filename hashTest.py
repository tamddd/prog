from collections import Counter
n = int(input())
s = Counter(list(input().split()))

q = int(input())
for _ in range(q):
    w = input()
    print(s[w])
