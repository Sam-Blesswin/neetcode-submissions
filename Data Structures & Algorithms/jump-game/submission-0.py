class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums)-1
        for j in range(len(nums)-2,-1,-1):
            if j+nums[j] >= dest:
                dest = j
        return dest == 0
        