class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        visited = set()
        y, x = 0, 0
        ret = []
        #右、下、左、上
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        i = 0
        while len(ret) != height*width:
            ret.append(matrix[y][x])
            visited.add((y, x))
            for _ in range(4):
                next_y = y + dy[i%4]
                next_x = x + dx[i%4]
                #はみ出さないし、訪れたことがないなら
                if 0 <= next_y < height and 0 <= next_x < width:
                    if (next_y, next_x) not in visited:
                        y = next_y
                        x = next_x
                        break
                i += 1
        return ret
