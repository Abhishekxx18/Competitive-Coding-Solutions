class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low,high = 0,len(arr)  - 1
        res = -1
        
        while low <= high:
            mid = (low + high ) // 2
            if arr[mid] == k:
                res = mid
                high = mid - 1
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return res