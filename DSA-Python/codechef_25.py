# Problem: Add Two Numbers (FLOW001)
# 
# Description:
# The task is very simple: given two integers A and B, write a program to add these two numbers and output it.
# 
# Input:
# The first line contains an integer T, the total number of test cases.
# Then follow T lines, each line contains two Integers A and B.
# 
# Output:
# For each test case, add A and B and display the sum in a new line.
# 
# Constraints:
# 1 <= T <= 1000
# 0 <= A, B <= 10000
# 
# Example:
# Input:
# 3
# 1 2
# 100 200
# 10 40
# 
# Output:
# 3
# 300
# 50

# Solution:

# Read the number of test cases
try:
    T = int(input())
    
    # Loop through each test case
    for _ in range(T):
        # Read A and B from the input line
        A, B = map(int, input().split())
        
        # Calculate and print the sum
        print(A + B)
except EOFError:
    pass