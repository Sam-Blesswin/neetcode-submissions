class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        zeroRow = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zeroRow = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if zeroRow:
            for j in range(n):
                matrix[0][j] = 0
