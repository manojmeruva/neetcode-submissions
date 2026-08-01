class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm1  = [0]*256
        
        if len(t)>len(s):
            return ""
        
        for i in t :
            hm1[ord(i)-ord('a')] +=1
        answer = ""
        mini = len(s)+1
        for i in range(len(s)):
            hm2 = [0]*256
            for j in range(i,len(s)):
                hm2[ord(s[j])-ord('a')]+=1
                if self.check(hm1,hm2):
                    if mini > (j-i+1):
                        answer = s[i:j+1]
                        
                        mini = len(answer)
                    break
            

        return answer
            



    def check(self, hm1, hm2):
        for i in range(256):
            if hm1[i]>0 and hm1[i]>hm2[i]:
                return False
        return True

        