#アルゴ式 リバーシ
n, m, y, x = map(int, input().split())
board = [list(input()) for _ in range(n)]

def reversi(board, y, x):
    dy = [1, 0, -1, 0, -1, -1, 1, 1]
    dx = [0, 1, 0, -1, 1, -1, -1, 1]
    board[y][x] = "o"
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        can = False
        whites = []
        
        while 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == ".":
                break
            elif board[ny][nx] == "x":
                whites.append([ny, nx])
            elif board[ny][nx] == "o":
                for yy, xx in whites:
                    board[yy][xx] = "o"
                break
            ny += dy[i]
            nx += dx[i]
    return board

for i in reversi(board, y, x):
    print("".join(i))
