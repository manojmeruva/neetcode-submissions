class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        answer = 0
        left = 0
        right = len(heights)-1

        while left < right:
            if heights[left]<heights[right]:
                answer = max(answer,heights[left]*(right-left))
                left+=1
            else:
                answer = max(answer,heights[right]*(right-left))
                right-=1
        
        return answer