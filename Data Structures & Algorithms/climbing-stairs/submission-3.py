class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp=[-1] * (n+1)
        def dfs(i:int):
            if i==0:
                return 1
            if i<0:
                return 0
            if self.dp[i] != -1:
                return self.dp[i]
            self.dp[i]= dfs(i-1) + dfs(i-2)
            return self.dp[i]
        return dfs(n)


        