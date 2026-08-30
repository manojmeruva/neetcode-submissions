from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)!=0 and val<=self.min_stack[-1]:
            self.min_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.min_stack[-1]
        
