# Given two sets A and B. check whether A is subset of B ?
# A is subset of B, if all elements of a set A are present in another set B.
# Example 1:
# Input:
# A = {1, 4, 3}
# B = {1, 4, 3, 2}
# Output: 
# True


class Solution:
    def checkSubset(self, A, B):
        return A.issubset(B)


#{ 
 # Driver Code Starts

def main():
    t = int(input())
    while(t > 0):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a=set(a);b=set(b);
        ob = Solution()
        res = ob.checkSubset(a,b)
        print(res)
        t-=1
        
if __name__ == "__main__": 
    main()
# } Driver Code Ends
