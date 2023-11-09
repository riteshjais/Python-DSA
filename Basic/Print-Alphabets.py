# Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line.

# Example 1:
# Input:
# c1 = 'a'
# c2 = 'z'
# Output: 
# a b c d e f g h i j k l m n o p q r s t u
# v w x y z
# Explanation:  Printed alphabets from a
# to z.

def alphabets(c1,c2):
    
    for i in range(ord(c1),ord(c2)+1):
        print(chr(i), end=" ")

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        c1 = input()
        c2 = input()
        
        alphabets(c1,c2)
        print() #This provides new line
