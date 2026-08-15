class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        topRow = 1

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:  
                        topRow = 0
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for r in range(1,m):
            for c in range(1,n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0


        if topRow == 0:
            for c in range(n):
                matrix[0][c] = 0
        
        