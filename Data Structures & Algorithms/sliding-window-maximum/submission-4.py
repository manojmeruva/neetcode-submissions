class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n<=k:
            nums.sort()
            return [nums[n-1]]
        heap = []
        answer = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        answer.append(-heap[0][0])
        left = 0
        for right in range(k,n):
            heapq.heappush(heap,(-nums[right],right))
            while heap[0][1] < left+1:
                heapq.heappop(heap)
            answer.append(-heap[0][0])
            left+=1
        return answer




