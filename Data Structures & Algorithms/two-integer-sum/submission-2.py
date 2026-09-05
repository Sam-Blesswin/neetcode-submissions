class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap=defaultdict(int)
        for i,n in enumerate(nums):
            rem = target - n
            if rem in hashmap:
                return [hashmap[rem],i]
            hashmap[n]=i
        return []

        