






Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume exactly one valid answer exists, and you cannot use the same element twice.

Example:
nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Answer (Optimal Approach):
Use a hash map (dictionary) to store number -> index while iterating.
For each number x, check if target - x is already in the map.
If yes, return the stored index and current index.

Python solution:
def two_sum(nums, target):
seen = {}
for i, x in enumerate(nums):
need = target - x
if need in seen:
return [seen[need], i]
seen[x] = i
return []

Time Complexity: O(n)
Space Complexity: O(n)