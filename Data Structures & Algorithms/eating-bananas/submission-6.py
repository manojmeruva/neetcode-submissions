class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        n = len(piles)
    
        if h==n:
            return piles[n-1]

        start = 1
        end = piles[n-1]
        minmid = 0
        while start<=end:
            mid = (start+end)//2
            curHours = 0
            for i in piles:

                if i%mid==0:
                    curHours+=i/mid
                else:
                    curHours = curHours+i//mid+1
            if curHours<=h:
                end=mid-1
                minmid = mid
            else:
                if start == end:
                    return minmid
                start = mid+1
        return minmid


        