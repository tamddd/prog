n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = len([i for i in range(n) if ab[i][0] < ab[i][1]])
print(ans)
