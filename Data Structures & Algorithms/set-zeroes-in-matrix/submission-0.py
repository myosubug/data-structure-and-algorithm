class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        zeros = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zeros.append([i,j])

        for a,b in zeros:
            self.applyZeroes(a,b, r, c, matrix)

    def applyZeroes(self, x, y, r, c, matrix):

        for i in range(r):
            matrix[i][y] = 0
        
        for j in range(c):
            matrix[x][j] = 0

