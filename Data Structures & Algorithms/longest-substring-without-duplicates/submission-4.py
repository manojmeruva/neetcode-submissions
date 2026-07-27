class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer  = 1
        charset = set(s)

        l = len(s)
        if len(charset) == l:
            return l
        for i in range(l):
            hm = set()
            for j in range(i,l):
                if s[j] in hm:
                    answer = max(answer,len(hm))
                    hm.clear()
                hm.add(s[j])
            answer = max(answer,len(hm))
        
        return answer





        