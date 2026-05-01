# Write a program to take a number from the user and print that number as Odd or Even.
# Test Case1:
# Input:
# 56
# Output:
# Even
# Test Case2:
# Input:
# 87
# Output:
# Odd

# Simple Approach
N=int(input())
if N%2==0:
    print("Even")
else:
    print("odd")

# Turnary Operator
N=int(input())
def Even_Odd_Check():
    print("Even" if N % 2 == 0 else "Odd")
Even_Odd_Check()

# Function
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check_even_odd(N))


# Bitwise operator
if N & 1 == 0:
    print("Even")
else:
    print("Odd")
