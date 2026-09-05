class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        for n in nums:
            hashset.add(n)
        res=0
        for n in hashset:
            if n-1 in hashset:
                continue
            count=0
            while n in hashset:
                n+=1
                count+=1
            res=max(res,count)
        return res

            
        