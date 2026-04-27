# Write a program to take two values from the user and swap them.
# Hint: You can use a third variable.
# Test Case1:
# Input:
# 12
# 4Output:
# 4
# 12
# Test Case2:
# Input:
# 99
# 45Output:
# 45
# 99

#----------------------------------------------------------------Approch

m,n=map(int,input().split())
def swap_no(m,n):
    m, n = n, m
    return m,n
print(*swap_no(m, n),sep="\n")


