from collections import deque
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = deque()
        result = [0]*len(t)
        for i in range(len(t)):
            while stack and t[i]>stack[-1][0]:
                popped = stack.pop()[1]
                days = i - popped
                result[popped] = days
            stack.append((t[i],i))
        return result
        