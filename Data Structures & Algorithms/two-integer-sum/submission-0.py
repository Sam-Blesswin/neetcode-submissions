class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            rem = target - n
            if rem in map:
                return [map[rem],i]
            map[n]=i
        return []
        