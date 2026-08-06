class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            nums = [0] * 26
            for ch in word:
                nums[ord(ch) - ord('a')] += 1
            key = tuple(nums)
            if key not in map:
                map[key]=[]
            map[key].append(word)
        return [val for key,val in map.items()]
            
        