# Given a tuple A with distinct elements and an integer X, 
# find the index position of X. Assume to have X in the tuple always.

# Example 1:

# Input:
# A = (1, 2, 3, 4, 5)
# X = 3
# Output: 
# 2

class Solution:
    def Index(self, A, X):
        return A.index(X)




#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    while(t > 0):
        A=tuple(map(int,input().split()))
        X = int(input())
        ob = Solution()
        res = ob.Index(A,X)
        print(res)
        t-=1
if __name__ == "__main__": 
    main()
# } Driver Code Ends
