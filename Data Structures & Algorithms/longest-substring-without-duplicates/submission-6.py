class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer  = 1
        charset = set(s)

        l = len(s)
        if len(charset) == l:
            return l
        
        hm = set()
        left  = 0
        for right in range(l):
            win = right-left+1
            if s[right] in hm:
                while s[left]!=s[right]:
                    hm.remove(s[left])
                    left+=1
                left+=1
            
            else:
                answer = max(answer,win)
            hm.add(s[right])
        
    
        return answer





        