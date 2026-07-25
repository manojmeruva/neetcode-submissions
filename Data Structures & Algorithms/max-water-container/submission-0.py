class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftmax = [0]*n
        rightmax = [0]*n
        a = 0
        for i in range(n):
            for j in range(i+1,n):
                a = max(min(heights[i],heights[j])*(j-i),a)
        return a
