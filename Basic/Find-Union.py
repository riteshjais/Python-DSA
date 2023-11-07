# Given two sets A and B. find the Union of both the sets.
# Input:
# A = {2, 5, 6}
# B = {1, 4, 3, 2}
# Output: 
# 1 2 3 4 5 6


class Solution:
    def Union(self, A, B):
        # ans=set()
        # for i in A:
        #     ans.add(i)
        # for i in B:
        #     ans.add(i)
        # return ans
        
        #Alternative method
        return A.union(B)


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    while(t > 0):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a=set(a);b=set(b);
        ob = Solution()
        res = ob.Union(a,b)
        for i in res:
            print(i,end = " ")
        print()
        t-=1
if __name__ == "__main__": 
    main()
# } Driver Code Ends
