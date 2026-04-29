# Write a program to take two numbers from the user and determine the greater of those two given numbers.
# Test Case1:
# Input:
# 20
# 3
# Output:
# 20
# Test Case2:
# Input:
# 5
# 7
# Output:
# 7 

A,B=map(int,input().split())
def grater_num():
    if A<B:
        print(B)
    else:
        print(A) 
grater_num()


