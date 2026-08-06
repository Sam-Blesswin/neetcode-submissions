class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) +"#"+ s
        return encoded

    def decode(self, s: str) -> List[str]:
        itr=0
        res=[]
        while itr < len(s):
            n=0
            while s[itr] != '#':
                n = n*10 + int(s[itr])
                itr+=1
            itr+=1
            res.append(s[itr:itr+n])
            itr+=n
        return res
