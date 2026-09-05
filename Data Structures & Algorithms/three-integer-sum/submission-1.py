class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k=0
        while k<len(nums):
            i=k+1
            j=len(nums)-1
            while i<j:
                sum = nums[i] + nums[j] +nums[k]
                if sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    i+=1
                    while i<j and nums[i-1]==nums[i]:
                        i+=1
                elif sum<0:
                    i+=1
                else:
                    j-=1
            k+=1
            while k<len(nums) and nums[k-1]==nums[k]:
                k+=1
        return res

        