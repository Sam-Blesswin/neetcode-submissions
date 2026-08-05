class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for s in strs:
            encodeStr += str(len(s))+"#"+s
        return encodeStr

    def decode(self, s: str) -> List[str]:
        res = []
        itr=0
        while itr<len(s):
            n = 0
            while itr<len(s):
                if s[itr] == '#':
                    break
                n = n*10 + int(s[itr])
                itr+=1
            itr+=1
            res.append(s[itr:(itr+n)])
            itr+=n
        return res
            
            


