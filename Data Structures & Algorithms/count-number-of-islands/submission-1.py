class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,m,n:int):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i-1,j,m,n)
            dfs(i+1,j,m,n)
            dfs(i,j-1,m,n)
            dfs(i,j+1,m,n)
            
        m,n=len(grid),len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j,m,n)
                    count+=1
        return count

        