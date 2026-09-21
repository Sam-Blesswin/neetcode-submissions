class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        has = [0] * 26

        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')]+=1
            has[ord(s2[i]) - ord('a')]+=1

        match = 0
        for i in range(26):
            if need[i] == has[i]:
                match+=1

        l=0
        r=len(s1)

        while r < len(s2):
            print(match)
            if match == 26:
                return True

            index = ord(s2[l]) - ord('a')
            if need[index] == has[index]:
                match -=1
            has[index] -= 1
            if need[index] == has[index]:
                match +=1
            l+=1

            index = ord(s2[r]) - ord('a')
            if need[index] == has[index]:
                match -=1
            has[index] += 1
            if need[index] == has[index]:
                match +=1
            r+=1
        
        return match == 26


        
        
    