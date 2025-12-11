#アルゴ式 フラグ値を、整数値にする
n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    cnt += (1 << i)
print(cnt)
