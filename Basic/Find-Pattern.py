# Given a string s, and a pattern p. 
# You need to find if p exists in s or not and return the starting index of p in s. 
# If p does not exist in s then -1 will be returned.
# Here p and s both are case-sensitive.
# Example 1:

# Input:
# s = "Hello"
# p = "llo"
# Output: 
# 2
# Explanation: llo starts from the second index in Hello.

def findPattern(s,p):
    return s.find(p)


def main():
    t=int(input())
    while(t>0):
        s=input()
        p=input()
        print(findPattern(s,p))
        t-=1

if __name__ == "__main__": 
    main()
