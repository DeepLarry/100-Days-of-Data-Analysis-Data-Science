# Armstrong Number

## Problem
Check whether a given number is an Armstrong number or not.

An Armstrong number is a number that is equal to the sum of its digits raised to the power of total number of digits.

Example:
153 → 1³ + 5³ + 3³ = 153 






n = int(input("Enter number: "))
temp = n
count = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")