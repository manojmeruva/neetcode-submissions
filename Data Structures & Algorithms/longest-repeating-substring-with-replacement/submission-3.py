class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 1
        l = len(s)
        if l<=1:
            return l
        for i in range(0,l):
            hm = {}
            maxv = 0
            for j in range(i,l):
                cl = j-i+1
                hm[s[j]] = hm.get(s[j],0) + 1
            
                maxv = max(maxv,hm[s[j]])

                dif = cl - maxv
                if k>=dif:
                    answer = max(answer,cl)
                    
        return answer

                
                
                

                



