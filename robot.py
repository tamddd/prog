h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]

n = int(input())
dy = {"L":-1, "R":1, "U":0, "D":0}
dx = {"L":0, "R":0, "U":-1, "D":1}
def check(x, y, act):
    ny = y + dy[act]
    nx = x + dx[act]
    if 0 <= nx < h and 0 <= ny < w:
        return s[nx][ny] != "#"
    else:
        return False

for act in input():
    if check(x, y, act):
        x = x + dx[act]
        y = y + dy[act]

print(x, y)
