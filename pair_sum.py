from bisect import bisect_left
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):
    cnt += n - bisect_left(a, k-a[i])
print(cnt)
