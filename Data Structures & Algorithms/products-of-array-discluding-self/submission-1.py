class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        prod=nums[n-1]
        for j in range(n-2,-1,-1):
            res[j] = res[j] * prod
            prod *= nums[j]
        return res




        