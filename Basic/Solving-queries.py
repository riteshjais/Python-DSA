# Given a dictionary, and a list of queries(keys), 
# you have to find and print the value of each query from the dictionary if present else it prints "None".
# Example 1:
# Input:
# dict = {1:"abc", 2: "cde", 3: "fgh"}
# query = [2, 3, 4]
# Output:
# cde
# fgh
# None


class Solution:
    def Query(self, dict, query):
        # for i in query:
        #     if i in dict:
        #         print(dict.get(i))
        #     else:
        #         print("None")
        
        #Alternative Method
        for i in query:
            print(dict.get(i))


#{ 
 # Driver Code Starts

def main():
    t = int(input())
    while(t > 0):
        a = list(map(int,input().split()))
        b = list(map(str,input().split()))
        query = list(map(int,input().split()))
        dict = {}
        for i in range(len(a)):
            dict[a[i]] = b[i]
        ob = Solution()
        res = ob.Query(dict,query)
        t-=1
if __name__ == "__main__": 
    main()
# } Driver Code Ends
