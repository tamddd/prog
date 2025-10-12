import csv


class sudokuSolver:
    def __init__(self):
        self.width = 9
        self.height = 9
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def solve(self):
        def _solve(index):
            if index == self.width * self.height:
                return True
            ny = index // 9
            nx = index % 9
            if self.board[ny][nx] != 0:
                return _solve(index + 1)

            for i in range(1, 10):
                self.board[ny][nx] = i
                if self.check(ny, nx) and _solve(index + 1):
                    return True
                self.board[ny][nx] = 0
            return False

        _solve(0)

    def check(self, y, x):
        # 縦,横
        vis = set()
        for i in range(self.height):
            num = self.board[i][x]
            if num == 0:
                continue
            if num in vis:
                return False
            vis.add(num)

        vis = set()
        for i in range(self.width):
            num = self.board[y][i]
            if num == 0:
                continue
            if num in vis:
                return False
            vis.add(num)

        # 3*3 左上、を求メル
        ry = (y // 3) * 3
        rx = (x // 3) * 3
        vis = set()
        for i in range(3):
            for j in range(3):
                num = self.board[ry + i][rx + j]
                if num == 0:
                    continue
                if num in vis:
                    return False
                vis.add(num)
        return True

    def show(self):
        for i in self.board:
            print(*i)

    def input_csv_board(self, csv_file_name):
        with open(csv_file_name, mode="r") as csv_file:
            reader = csv.reader(csv_file)
            self.board = []
            for row in reader:
                self.board.append(list(map(int, row)))


def main():
    ssol = sudokuSolver()
    ssol.input_csv_board("sudoku_input.csv")
    ssol.solve()
    ssol.show()


if __name__ == "__main__":
    main()
