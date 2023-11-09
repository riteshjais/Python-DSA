# Given a string s, you need to slice it so that the output is a substring that contains all the chracters 
# except first and last. The length of the s will be greater than 2.

# Example 1:
# Input:
# s = "Hello"
# Output: 
# ell
# Explanation: The first and last character
# are ignored.

def sliceString(s):
    return s[1:-1]





def main():
    t=int(input())
    while(t>0):
        s=input()
        print(sliceString(s))
        t-=1

if __name__ == "__main__": 
    main()
