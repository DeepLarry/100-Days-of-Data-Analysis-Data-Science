# Cute Substrings
# A string whose length is odd is said to be cute if:

# Every character at an odd index (i.e. the 
# 1
# 1-st, 
# 3
# 3-rd, 
# 5
# 5-th, ... from the beginning) is either the letter 'u' or the letter 'o'; and
# Every character at an even index (i.e. the 
# 2
# 2-nd, 
# 4
# 4-th, 
# 6
# 6-th, ... from the beginning) is the letter 'w'.
# For example, 
# uwu
# ,
# o
# ,
# owuwo
# ,
# uwowuwo
# uwu,o,owuwo,uwowuwo are examples of cute strings, while 
# uwuw
# ,
# uwe
# ,
# ono
# uwuw,uwe,ono are not cute.

# You are given a string 
# S
# S of length 
# N
# N, containing only lowercase English letters.
# Find the length of the longest contiguous substring of 
# S
# S that's cute.

# That is, find the largest possible value of 
# (
# R
# −
# L
# +
# 1
# )
# (R−L+1) across all pairs 
# (
# L
# ,
# R
# )
# (L,R) such that the string
# S
# L
# S
# L
# +
# 1
# …
# S
# R
# S 
# L
# ​
#  S 
# L+1
# ​
#  …S 
# R
# ​
#   is cute.

# It's possible that no contiguous substring of 
# S
# S is cute, in which case you must output 
# 0
# 0.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of two lines of input.
# The first line of each test case contains a single integer 
# N
# N, denoting the length of the given string.
# The second line contains the string 
# S
# S of length 
# N
# N.
# Output Format
# For each test case, output on a new line the length of the longest cute substring of 
# S
# S.

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# S
# S consists of 
# N
# N lowercase English letters, i.e. the characters {a, b, c, ..., z} (ASCII values 
# 97
# 97 to 
# 122
# 122, inclusive.)
# Sample 1:
# Input
# Output
# 5
# 3
# uwu
# 5
# powor
# 6
# muwowu
# 4
# owpo
# 6
# winter
# 3
# 3
# 5
# 1
# 0
# Explanation:
# Test case 
# 1
# 1: The entire string 
# uwu
# uwu is cute, with length 
# 3
# 3.

# Test case 
# 2
# 2: The substring 
# owo
# owo from index 
# 2
# 2 to index 
# 4
# 4, having length 
# 3
# 3, is the longest cute substring.

# Test case 
# 3
# 3: The substring 
# uwowu
# uwowu from index 
# 2
# 2 to index 
# 6
# 6, having length 
# 5
# 5, is the longest cute substring.

# Test case 
# 4
# 4: The substring 
# o
# o at index 
# 4
# 4 is the longest cute substring.
# Note that 
# ow
# ow is not a cute substring because it doesn't have odd length.

# Test case 
# 5
# 5: There are no cute substrings in 
# winter
# winter, so we output 
# 0
# 0.

# My approach: 
# cook your dish here
def is_cute(sub):
    # length odd hona chahiye
    if len(sub) % 2 == 0:
        return False
    
    for i in range(len(sub)):
        if i % 2 == 0:  # 0-based -> odd position (1st, 3rd...)
            if sub[i] not in ['u', 'o']:
                return False
        else:  # even position
            if sub[i] != 'w':
                return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    max_len = 0
    
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if is_cute(sub):
                max_len = max(max_len, len(sub))
    
    print(max_len)