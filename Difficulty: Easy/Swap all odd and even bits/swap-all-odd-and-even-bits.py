#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        even = 0xAAAAAAAA
        odd =  0x55555555
        
        evena = ( n & even ) >> 1
        odda = ( n & odd ) << 1
        ans = evena | odda
        return ans





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends