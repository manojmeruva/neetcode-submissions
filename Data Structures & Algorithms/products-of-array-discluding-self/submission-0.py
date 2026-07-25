class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefixprod = [1]*n
        output=[]
        suffixprod = [1]*n
        for i in range(1,n):
            prefixprod[i] = nums[i-1]*prefixprod[i-1]
            suffixprod[n-i-1] = nums[n-i]*suffixprod[n-i]
        
        for i in range(n):
            output.append(prefixprod[i]*suffixprod[i])
        

        return output
