class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map={}
        l=0
        res = 0
        for r,ch in enumerate(s):
            if ch in map:
                if l<=map[ch]:
                    l=map[ch]+1
            map[ch] = r
            res = max(res, r-l+1)
        return res

            
        