class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm1  = [0]*256
        hm2 = [0]*256
        if len(t)>len(s):
            return ""
        
        for i in t :
            hm1[ord(i)-ord('a')] +=1
        answer = ""
        mini = len(s)+1
        for i in range(len(t)-1):
            hm2[ord(s[i])-ord('a')]+=1
        left = 0
        mini = len(s)+1
        for j in range(len(t)-1,len(s)):
            hm2[ord(s[j])-ord('a')]+=1
            while self.check(hm1,hm2):
            
                if mini>j-left+1:
                    answer = s[left:j+1]
                    mini = len(answer)
                hm2[ord(s[left])-ord('a')]-=1
                left+=1

        

        return answer
            



    def check(self, hm1, hm2):
        for i in range(256):
            if hm1[i]>0 and hm1[i]>hm2[i]:
                return False
        return True

        