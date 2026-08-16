class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(nums))]
        def dfs(itr,end,flag:int) -> int:
            if itr >= end:
                return 0
            if dp[itr][flag] != -1:
                return dp[itr][flag]
            dp[itr][flag] = max(nums[itr] + dfs(itr+2, end, flag), dfs(itr+1, end, flag))
            return dp[itr][flag]
        if len(nums) == 1:
            return nums[0]
            
        return max(dfs(0, len(nums)-1, 0), dfs(1, len(nums),1))

        