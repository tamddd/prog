n, m, y, x = map(int, input().split())
board = [input() for _ in range(n)]

def can_place(board, y, x):
    dy = [1, 0, -1, 0, -1, -1, 1, 1]
    dx = [0, 1, 0, -1, 1, -1, -1, 1]

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        white = False
        can = False
        while 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == ".":
                break
            elif board[ny][nx] == "x":
                white = True
            elif board[ny][nx] == "o":
                can = white
                break
            ny += dy[i]
            nx += dx[i]

        if can:
            return True
    return False

print("Yes" if can_place(board, y, x) else "No")
