class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = float('-inf')
        for n in nums:
            sum += n
            maxSum = max(sum, maxSum)
            if sum < 0:
                sum = 0
        return maxSum
        