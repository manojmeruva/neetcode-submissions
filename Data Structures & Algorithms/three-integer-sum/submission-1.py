class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = set()
        if n < 3:
            return []
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    summ=nums[j]+nums[i]+nums[k]
                    if summ==0:
                        output.add((nums[i],nums[j],nums[k]))
        res = []
        for r in output:
            res.append(list(r))
        return res
        
