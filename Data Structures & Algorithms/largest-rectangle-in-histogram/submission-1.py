from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = deque()
        n = len(heights)
        leftmin = [-1]*n
        rightmin = [n]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftmin[i] = stack[-1]
            stack.append(i)
        
        stack = deque()
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rightmin[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            area = (rightmin[i]-1-leftmin[i])*heights[i]
            maxarea = max(maxarea,area)
            
        return maxarea