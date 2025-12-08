#アルゴ式 部下の人数
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

n, x = map(int, input().split())
p = list(map(int, input().split()))
staffs = defaultdict(list)
for i, v in enumerate(p):
    staffs[v].append(i+1)

def staff_count(x, staffs):
    """
    for i in staffs[x]:
        cnt += solver(i, staffs)
    return cnt
    """
    return sum([1+staff_count(i, staffs) for i in staffs[x]])
print(staff_count(x, staffs))
