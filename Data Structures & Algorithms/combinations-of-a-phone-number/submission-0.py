class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def dfs(itr, word):
            if itr == len(digits):
                res.append(word)
                return

            keys = digitToChar[digits[itr]]
            for i in range(len(keys)):
                dfs(itr+1, word + keys[i])

        dfs(0,"")
        return res

