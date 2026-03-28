Question
You are given an integer array nums.
For each index i, find the first element when moving right in circular manner whose total frequency in nums is strictly greater than frequency of nums[i].
If no such element exists, answer is -1 for that position.

Example
nums = [3, 1, 1, 2, 3, 3, 2]

Frequencies:
3 -> 3 times
1 -> 2 times
2 -> 2 times

Output:
[-1, 3, 3, 3, -1, -1, 3]

Why:
For value 1 (freq 2), next element with higher freq is 3 (freq 3).
For value 3 (freq 3), no element has higher freq, so -1.

Answer Approach

Precompute frequencies with a hash map.
Use a monotonic stack of indices, similar to Next Greater Element in circular array.
Traverse 2n times from right to left using i % n.
Pop stack while top does not have strictly higher frequency.
Stack top (if exists) is the answer for current index.
Push current index.

------>Time Complexity: O(n)
------>Space Complexity: O(n)

from collections import Counter

def next_greater_frequency_circular(nums):
    n = len(nums)
    freq = Counter(nums)
    ans = [-1] * n
    stack = []  # stores indices, maintained by decreasing frequency of nums[index]

    for i in range(2 * n - 1, -1, -1):
        idx = i % n
        cur_freq = freq[nums[idx]]

        while stack and freq[nums[stack[-1]]] <= cur_freq:
            stack.pop()

        if stack:
            ans[idx] = nums[stack[-1]]

        stack.append(idx)
    return ans

# demo
nums = [3, 1, 1, 2, 3, 3, 2]
print(next_greater_frequency_circular(nums))  # [-1, 3, 3, 3, -1, -1, 3]ṇ
