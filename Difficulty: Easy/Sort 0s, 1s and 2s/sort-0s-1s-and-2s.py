#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        l,m,h=0,0,len(arr)-1
        while m<=h:
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
                
            elif arr[m]==1:
                m+=1
            else:
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
        return arr
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends