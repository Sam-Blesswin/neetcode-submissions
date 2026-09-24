class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        k=r
        while l<=r:
            mid = (l+r)//2
            hour = 0
            for n in piles:
                hour += math.ceil(n/mid)
            if hour <= h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k
         