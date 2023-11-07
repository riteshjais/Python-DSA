# Given a tuple A , find if all elements of tuple are different or not.

# Example 1:

# Input:
# A = (1, 2, 3, 4, 5, 4)
# Output: 
# Not Distinct

class Solution:
    def checkDistinct(self, A):
        if(len(A)==len(set(A))):
            return "Distinct"
        else:
            return "Not Distinct"
    

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    while(t > 0):
        a=tuple(map(int,input().split()))
        ob = Solution()
        res = ob.checkDistinct(a)
        print(res)
        t-=1
if __name__ == "__main__": 
    main()
# } Driver Code Ends
