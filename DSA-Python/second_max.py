Q.) Finding Maximum, Second Maximum, Third, and Fourth (Without Using Methods)


Solved:
Flow chart based probelm Solved.

Time Complexity: O(1)

Reason:
The program always performs a fixed number of comparisons.
It does not depend on input size because we only handle 4 numbers.
Number of comparisons is constant.

Space Complexity: O(1)
We only store a few variables.




a, b, c, d = map(int, input("Enter four numbers: ").split())
if a > b:
    max1 = a
    max2 = b
else:
    max1 = b
    max2 = a
if c > max1:
    max3 = max2
    max2 = max1
    max1 = c
elif c > max2:
    max3 = max2
    max2 = c
else:
    max3 = c

if d > max1:
    max4 = max3
    max3 = max2
    max2 = max1
    max1 = d
elif d > max2:
    max4 = max3
    max3 = max2
    max2 = d
elif d > max3:
    max4 = max3
    max3 = d
else:
    max4 = d
print("Max:", max1)
print("Second Max:", max2)
print("Third Max:", max3)
print("Fourth Max:", max4)



Q.)------Finding Max, Second Max, Third, Fourth (Using Methods)

Solved:
Time Complexity:
O(n log n)

Reason:
Python uses Timsort algorithm, which is very efficient.

Space Complexity:
O(n)
Because we store numbers in a list.

nums = list(map(int, input("Enter four numbers: ").split()))
nums.sort(reverse=True)
print("Max:", nums[0])
print("Second Max:", nums[1])
print("Third Max:", nums[2])
print("Fourth Max:", nums[3])