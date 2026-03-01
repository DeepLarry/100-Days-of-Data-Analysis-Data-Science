"""
DSA Pattern Problem
Title: Diamond Pattern using While Loop
Difficulty: Easy
Topic: Patterns / Loops

Description:
Write a Python program to print a diamond star pattern using while loops.

Example:
Input:
5


"""


n = int(input("Enter number of rows: "))
i = 1
while i <= n:
    space = 1
    while space <= n - i:
        print(" ", end="")
        space += 1

    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()
    i += 1


i = n - 1
while i >= 1:
    space = 1
    while space <= n - i:
        print(" ", end="")
        space += 1

    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    print()
    i -= 1


'''
Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

Approach:
1. Firstly print the upper half of the diamond.
2. Then print the lower half of the diamond.
3. Using nested while loops for spaces and stars.

Time Complexity: O(n^2)
Space Complexity: O(1)


    
 Author: Deep (DSA Practice)
'''