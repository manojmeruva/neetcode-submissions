class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        hm1 = [0]*26
        hm2 = [0]*26
        for i in range(0,len(s1)):
            index1 = ord(s1[i])-ord('a') 
            hm1[index1] += 1
            index2 = ord(s2[i]) - ord('a')
            hm2[index2] += 1
        left =0
        for right in range(len(s1),len(s2)):
            if self.checkEqual(hm1,hm2):
                return True
            hm2[ord(s2[right])-ord('a')] += 1
            hm2[ord(s2[left])-ord('a')] -= 1
            # print(hm1,hm2)
            left+=1
        
        return self.checkEqual(hm1,hm2)
    
    def checkEqual(self,hm1,hm2):
        for i in range(26):
            if hm1[i]!=hm2[i]:
                return False
        return True
            

            
            

            

        