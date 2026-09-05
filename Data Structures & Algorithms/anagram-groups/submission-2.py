class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        hashmap=defaultdict(str)
        for word in strs:
            bucket=[0]*26
            for ch in word:
                bucket[ord(ch) - ord('a')] += 1
            key=tuple(bucket)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(word)
        return [v for k,v in hashmap.items()]



        