class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(i:int, j:int) -> int:
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            count = dfs(i+1,j)
            count+=dfs(i,j+1)

            dp[i][j] = count

            return count
        return dfs(0,0)
        