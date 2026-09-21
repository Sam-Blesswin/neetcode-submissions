class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")

        prod_1 = 1
        prod_2 = 1

        for i in range(len(nums)):
            prod_1 *= nums[i]
            prod_2 *= nums[len(nums)-1-i]

            res = max(res,max(prod_1, prod_2))

            if prod_1 == 0:
                prod_1 = 1
            if prod_2 == 0:
                prod_2 = 1
                
        return res
        