class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i,e,flag:int) -> int:
            if i >= e:
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            dp[i][flag] = max(nums[i] + dfs(i+2, e, flag), dfs(i+1,e, flag))
            return dp[i][flag]
        return max(dfs(0, len(nums)-1, 0), dfs(1, len(nums), 1))

        