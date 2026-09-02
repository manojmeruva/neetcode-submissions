class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top  = 0
        bottom = len(matrix) - 1
        m = len(matrix[0])
        while top <= bottom:
            row = (top+bottom)//2
            if matrix[row][m-1]<target:
                top = row+1
            elif matrix[row][0] > target:
                bottom = row-1
            else:
                return self.binarySearch(0,m-1,matrix[row],target)
        return False
    
    def binarySearch(self,s,e,arr,target):
        while s <=e:
            m = (s+e)//2
            if arr[m]==target:
                return True
            elif arr[m]>target:
                e = m -1
            else:
                s = m+1
        return False

        