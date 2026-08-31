from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        count =1
        stack = deque()
        minTime = (target -pairs[0][0])/pairs[0][1]
        for i in pairs:
            curtime = (target-i[0])/i[1]
            if curtime>minTime:
                count+=1
                minTime = curtime
            
        return count

        