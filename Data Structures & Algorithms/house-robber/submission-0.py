class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums))
        def dfs(itr:int) -> int:
            if itr >= len(nums):
                return 0
            if dp[itr] != -1:
                return dp[itr]
            dp[itr] = max(nums[itr] + dfs(itr+2), dfs(itr+1))
            return dp[itr]
        return dfs(0)
        