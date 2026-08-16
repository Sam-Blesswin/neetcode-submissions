class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def dfs(itr:int) -> int:
            if itr == n:
                return 1
            if itr > n:
                return 0
            if dp[itr] != -1:
                return dp[itr]
            dp[itr] = dfs(itr+1) + dfs(itr+2)
            return dp[itr]
        return dfs(0)