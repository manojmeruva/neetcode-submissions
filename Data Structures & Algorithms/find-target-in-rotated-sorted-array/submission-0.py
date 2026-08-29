class Solution:
    def search(self, arr, key):
        # code here
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == key:
                return mid
                
            if arr[left]<=arr[mid]:
                if arr[left]<=key and arr[mid]>=key:
                    right = mid -1
                
                else:
                    left = mid+1
            
            else:
                if arr[mid]<=key and arr[right]>=key:
                    left = mid+1
                else:
                    right = mid-1
        return -1
                