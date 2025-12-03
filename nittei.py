#アルゴ式 旅行の日程

n, m, k = map(int, input().split())
d = set(map(int, input().split()))

for i in range(n-k+1):
    flg = True
    for j in range(i, i+k):
        if j not in d:
            continue
        else:
            flg = False
    if flg:
        print("Yes")
        exit()
print("No")
