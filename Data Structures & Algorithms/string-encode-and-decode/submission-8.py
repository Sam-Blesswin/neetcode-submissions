class Solution:

    def encode(self, strs: List[str]) -> str:
        key=""
        for s in strs:
            key += f"{len(s)}#{s}"
        return key

    def decode(self, s: str) -> List[str]:
        print(s)
        res=[]
        itr = 0
        while itr<len(s):
            num = 0
            while s[itr] != '#':
                num=(num*10)+int(s[itr])
                itr+=1
            itr+=1
            res.append(s[itr:itr+num])
            itr+=num
        return res
