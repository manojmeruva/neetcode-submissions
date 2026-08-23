class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        answer = 0
        n = len(prices)
        while right < n:
            if prices[left]-prices[right]>0:
                left=right
            else:
                answer = max(answer,prices[right]-prices[left])
            right+=1
        return answer


        