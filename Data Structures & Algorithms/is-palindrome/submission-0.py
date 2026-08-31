class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9'):
                st+=i
        print(st)
        left = 0
        right = len(st)-1
        while left<right:
            
            if st[left].lower()!=st[right].lower():
                return False
            left+=1
            right-=1
        return True

        