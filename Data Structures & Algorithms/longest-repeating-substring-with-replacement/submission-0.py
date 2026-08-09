class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = defaultdict(int)
        l=0
        maxVal = 0
        res = 0
        for r,ch in enumerate(s):
            map[ch] += 1
            maxVal = max(maxVal, map[ch])
            while (r-l+1) - maxVal > k:
                map[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res




        