# [LC_array-with-elements-not-equal-to-average-of-neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors)

Return any rearrangement of nums such that every element in rearranged array is not equal to average of its neighbors

```txt
Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]

Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
```

## Solution

```py
def rearrangeArray(self, A: list):
  A.sort()
  for i in range(1, len(A), 2):
    A[i], A[i - 1] = A[i - 1], A[i]
  return A
```
