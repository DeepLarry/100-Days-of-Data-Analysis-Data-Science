# Write a program to take two numbers, A and B from the user. 
# Your task is to find the largest number that is less than A and can be
# divided evenly by B. Can you figure out that number?
# Test Case1:
# Input:
# 15
# 4
# Output:
# 12
# Test Case2:
# Input:
# 27
# 5
# Output:
# 25

A,B=map(int,input().split())
def A_largest_num_Div_B():
   k=A%B
   J=A-k
   print(J)
A_largest_num_Div_B()

