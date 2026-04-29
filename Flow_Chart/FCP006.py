# Write a program to take a positive number from the user and then display the last digit of that number.

# Test Case1:
# Input:
# 843 Output:
# 3
# Test Case2:
# Input:
# 321 Output:
# 1 
N=int(input())
def last_digit():
    X=N%10
    print(X)
last_digit()
  