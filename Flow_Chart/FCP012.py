# Write a program to take a number from the user and output whether that number is negative, positive or zero.
# Test Case1:
# Input:
# 6
# Output:
# Positive
# Test Case2:
# Input:
# 0
# Output:
# Zero

N=int(input())
def Check_Positive_Neagative_Zero(n):
   return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(Check_Positive_Neagative_Zero(N))
