class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,itr)->bool:
            if itr==len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            if board[i][j] == '#' or board[i][j] != word[itr]:
                return False

            ch = board[i][j]
            board[i][j] = '#'
            status = dfs(i-1,j,itr+1) or dfs(i+1,j,itr+1) or dfs(i,j-1,itr+1) or dfs(i,j+1,itr+1)
            board[i][j] = ch
            return status

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        