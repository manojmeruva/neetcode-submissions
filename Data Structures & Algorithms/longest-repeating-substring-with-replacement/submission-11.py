import gc
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 1
        l = len(s)
        if l <= 1:
            return l
        hm = {}
    
        left = 0
        right = 0
        count = 0
        maxf = 0
        while left <= right and right < l:
            win = right - left + 1
            cs = s[right]
            hm[cs] = hm.get(cs,0) + 1
            maxf = max(maxf,hm[cs])
            if win - maxf <= k:
                answer = max(answer, win)
            else:
                hm[s[left]]-=1
                left += 1
            right+=1
        gc.collect()
                

        return answer
