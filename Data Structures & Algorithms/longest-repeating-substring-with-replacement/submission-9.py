import gc
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 1
        l = len(s)
        if l <= 1:
            return l
        charset = set(s)
        sl = len(charset)
        for i in charset:
            left = 0
            right = 0
            count = 0
            while left <= right and right < l:
                win = right - left + 1
                if s[right] == i:
                    count += 1
                if win - count <= k:
                    answer = max(answer, win)
                else:
                    if s[left] == i:
                        count-=1
                    left += 1
                right+=1
            gc.collect()
                    

        return answer
