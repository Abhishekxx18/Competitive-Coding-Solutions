class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if arr[mid] == 1:
                mid += 1
                
            elif arr[mid]  == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low += 1
                mid += 1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1        