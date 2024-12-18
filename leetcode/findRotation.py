class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        all_rotate = [True] * 4

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[j][n-i-1]:
                    all_rotate[0] = False

                if mat[i][j] != target[n-i-1][n-j-1]:
                    all_rotate[1] = False

                if mat[i][j] != target[n-j-1][i]:
                    all_rotate[2] = False

                if mat[i][j] != target[i][j]:
                    all_rotate[3] = False

        return any(all_rotate)
