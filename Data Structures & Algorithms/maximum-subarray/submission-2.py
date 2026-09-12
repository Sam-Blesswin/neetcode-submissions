class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        sum = 0
        for n in nums:
            sum += n
            res = max(res,sum)
            if sum < 0:
                sum=0
        return res
        