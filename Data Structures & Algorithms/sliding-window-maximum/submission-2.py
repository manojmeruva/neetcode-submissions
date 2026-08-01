class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=k:
            nums.sort()
            return [nums[len(nums)-1]]
        answer = []
        for i in range(len(nums)-k+1):
            window = []
            for j in range(i,i+k):
                window.append(nums[j])
            window.sort()
            answer.append(window[len(window)-1])
        return answer


