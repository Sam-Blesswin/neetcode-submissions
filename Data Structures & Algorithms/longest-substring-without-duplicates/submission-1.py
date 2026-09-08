class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap=defaultdict(str)
        res=0
        l=0
        for r,ch in enumerate(s):
            if ch in hashmap:
                if l <= hashmap[ch]:
                    l=hashmap[ch]+1
            hashmap[ch] = r
            res = max(res, r-l+1)
        return res

            