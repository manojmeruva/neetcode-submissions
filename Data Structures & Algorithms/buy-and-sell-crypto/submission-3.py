class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = len(prices)-1
        answer = 0
        for i in range(right+1):
            dif = 0
            for j in range(i+1,right+1):
                dif = prices[j]-prices[i]
                answer = max(answer,dif)
        
        return answer


        