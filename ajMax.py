n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] <= a[j] and a[k] <= a[j]:
                cnt += 1

print(cnt)
