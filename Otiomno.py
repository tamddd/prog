n = int(input())
board = [list(input()) for _ in range(n)]

class OTIMONO:
    def __init__(self, height, board):
        self.height = height
        self.width = 5
        self.board = board

    def erase(self, l):
        for y, x in l:
            self.board[y][x] = "0"
        
        for x in range(self.width):
            new_col = []
            for y in reversed(range(self.height)):
                if self.board[y][x] != "0":
                    new_col.append(self.board[y][x])
            
            for y in reversed(range(self.height)):
                if len(new_col) > 0:
                    self.board[y][x] = new_col.pop(0)
                else:
                    self.board[y][x] = "0"

    def getErasable(self):
        erasablePositions = set()
        for i in range(self.height):
            for j in range(self.width):
                if j + 2 < self.width:
                    if self.board[i][j] == "0":
                        continue
                    if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2]:
                        for jj in range(j, j+3):
                            erasablePositions.add((i, jj))
        return erasablePositions

    def game(self):
        while True:
            erasePos = self.getErasable()
            if len(erasePos) == 0:
                break
            else:
                self.erase(erasePos)
        self.printBoard()

    def printBoard(self):
        for i in self.board:
            print("".join(i))

game = OTIMONO(n, board)
game.game()
