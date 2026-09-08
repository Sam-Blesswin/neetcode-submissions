class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap=defaultdict(int)
        res=0
        maxRep=0
        l=0

        for r,ch in enumerate(s):
            hashmap[ch]+=1
            maxRep = max(maxRep, hashmap[ch])

            while (r-l+1) - maxRep > k:
                hashmap[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        return res
            


        
        