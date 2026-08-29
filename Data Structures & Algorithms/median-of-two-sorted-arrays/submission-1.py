class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        an = len(a)
        bn = len(b)
        k = (an+bn)//2
        answer = self.binarySearch(a,b,k) if an<bn else self.binarySearch(b,a,k)
        return answer
        
    
    def binarySearch(self,a,b,k):
        an = len(a)
        bn = len(b)
        s = max(k-bn,0)
        e = min(k,an)
        answer = 0
        while s<=e:
            mid1 = (s+e)//2
            mid2 = k-mid1
            l1 = a[mid1-1] if mid1>0 else -float('inf')
            r1 = a[mid1] if mid1<an else float('inf')
            l2 = b[mid2-1] if mid2>0 else -float('inf')
            r2 = b[mid2] if mid2<bn else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                if (an+bn)%2==1 :
                    return min(r1,r2)
                maxl = max(l1,l2)
                maxr = min(r1,r2)
                answer = (maxl+maxr)/2
                break

            elif l1 > r2:
                e = mid1 - 1

            else:
                s = mid1 + 1
        
        return answer
        
            
        