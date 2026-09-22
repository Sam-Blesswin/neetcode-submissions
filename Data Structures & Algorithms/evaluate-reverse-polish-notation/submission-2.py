class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                b,a = stack.pop(), stack.pop()
                stack.append(a+b)
            elif ch == "-":
                b,a = stack.pop(), stack.pop()
                stack.append(a-b)
            elif ch == "*":
                b,a = stack.pop(), stack.pop()
                stack.append(a*b)
            elif ch == "/":
                b,a = stack.pop(), stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(ch))
        return stack[-1]
        