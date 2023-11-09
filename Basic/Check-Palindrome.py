# Given a string s, you need to check if it is palindrome or not. 
# A palidrome is a string that reads the same from front and back. Ignore the case in this question.

# Example 1:
# Input:
# s = "Hello"
# Output: 
# False
# Explanation: Hello is not equal to olleH
# so it's not a palindrome.

def isPalin(s):
    s=s.lower()
    rev=s[::-1]
    return s==rev



def main():
    t=int(input())
    while(t>0):
        s=input()
        print(isPalin(s))
        t-=1

if __name__ == "__main__": 
    main()
