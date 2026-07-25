class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        heap = []
        for i,n in hashmap.items():
            heapq.heappush(heap,(n,i))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in heap:
            output.append(i[1])
        return output