# [LC_two-sum-ii-input-array-is-sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

Find two indices that sum up to target in sorted array

```txt
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

## Solution

```py
def twoSum1(self, numbers, target):
  l, r = 0, len(numbers) - 1
  while l < r:
    s = numbers[l] + numbers[r]
    if s == target:
      return [l + 1, r + 1]
    elif s < target:
      l += 1
    else:
      r -= 1
```
