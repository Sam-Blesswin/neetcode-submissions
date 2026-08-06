class Solution:
    def isValid(self, s: str) -> bool:
        map={']':'[','}':'{',')':'('}
        stack=[]
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif not stack:
                return False
            elif stack.pop() != map[ch]:
                return False
        return not stack

        