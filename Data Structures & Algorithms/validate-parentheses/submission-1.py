class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        hashmap = {']':'[', '}':'{',')':'('}
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif not stack:
                return False
            elif stack[-1] != hashmap[ch]:
                return False
            else:
                stack.pop()
        return not stack


        