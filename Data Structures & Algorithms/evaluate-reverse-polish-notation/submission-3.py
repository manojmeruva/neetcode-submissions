from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i in "+-*/":
                first = int(stack.pop())
                second = int(stack.pop())
                if i == "+":
                    stack.append(second+first)
                if i == "*":
                    stack.append(second*first)
                if i == "-":
                    stack.append(second-first)
                if i == "/":
                    stack.append(second/first)
            else:
                stack.append(i)
        return int(stack[-1])