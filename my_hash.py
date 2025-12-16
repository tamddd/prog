from collections import Counter
n = input()
words = list(input().split())
MOD = 1000003

def my_hash(word):
    k = 30
    res = 0
    for i, c in enumerate(reversed(word)):
        res += (ord(c) - ord('a') + 1) * (30**i)
        res %= MOD
    return res
c = Counter(map(my_hash, words))
ans = sorted(c.items(), key=lambda x : x[1])[-1][1]
print(ans)
