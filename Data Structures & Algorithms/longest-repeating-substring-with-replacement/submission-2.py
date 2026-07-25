class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        answer = 1
        l = len(s)
        if l<=1:
            return l
        for i in range(0,l):
            cs = s[i]
            hm[s[i]] = 1
            ca = 1
            for j in range(i+1,l):
                css = cs + s[j]
                cl = j-i+1
                hm[s[j]] = hm.get(s[j],0) + 1
            
                maxv = max(hm.values())

                dif = cl - maxv
                if k>=dif:
                    answer = max(answer,cl)
                    
            hm.clear()
        return answer

                
                
                

                



