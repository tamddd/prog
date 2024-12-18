class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        #右上から
        diagonal_sum = 0
        for i in range(n):
            diagonal_sum += mat[i][i]
            #重複を足さないように０にする
            mat[i][i] = 0
        #左上から
        for i in range(n):
            diagonal_sum += mat[i][n-i-1]
        return diagonal_sum
