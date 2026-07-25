class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        maxi = 0
        for i in store:
            streak = 1
            cur = i
            while cur+1 in store:
                streak += 1
                cur+=1
            maxi = max(maxi,streak)
        return maxi    
        