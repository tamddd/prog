#アルゴ式 部分和問題

n, x = map(int, input().split())
a = list(map(int, input().split()))

def solver(tot, idx):
    if idx == n:
        return tot == 0
    else:
        return solver(tot-a[idx], idx+1) or solver(tot, idx+1)
print("Yes" if solver(x, 0) else "No")
