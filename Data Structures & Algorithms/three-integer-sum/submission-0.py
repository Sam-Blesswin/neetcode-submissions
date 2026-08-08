class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        res = []
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j-1] == nums[j]:
                        j+=1
                elif sum < 0:
                    j+=1
                else:
                    k-=1
            i+=1
            while i<len(nums) and nums[i-1] == nums[i]:
                i+=1
        return res

                


