#アルゴ式 ２番目の最大値
n = int(input())
a = list(sorted(list(map(int, input().split()))))
a.pop()
print(a.pop())
