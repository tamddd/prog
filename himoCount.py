import bisect
#アルゴ式 紐の本数

n = int(input())
l = list(map(int, input().split()))
l.sort()

q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    b += 1

    a_pos = bisect.bisect_left(l, a)
    b_pos = bisect.bisect_left(l, b)
    print(b_pos - a_pos)
