# Write a program to take two numbers A and B from the user and calculate the quotient and remainder when number A is divided by
# number B.
# Note: Print the output in the order as mentioned in the question.
# Test Case1:
# Input:
# 12
# 5Output:
# 2
# 2
# Test Case2:
# Input:
# 15
# 6Output:
# 2
# 3 Arithmetic Operators No
# FCP00
# Write a program

A,B=map(int,input().split())
def calculate_Que_Rem():
    C=A%B
    D=A//B
    print("quotient : ",C)
    print("Remainder : ",D)
calculate_Que_Rem()


