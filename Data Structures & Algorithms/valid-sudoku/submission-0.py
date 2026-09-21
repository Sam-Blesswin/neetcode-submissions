class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        gridMap = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowMap[i]:
                    return False
                if board[i][j] in colMap[j]:
                    return False
                if board[i][j] in gridMap[(i//3, j//3)]:
                    return False

                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                gridMap[(i//3, j//3)].add(board[i][j])
        
        return True
        
