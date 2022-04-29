# [LC_can-place-flowers](https://leetcode.com/problems/can-place-flowers)

Flowers cannot be planted in adjacent plots
Given an integer array flowerbed containing 0's, 1's, where 0 means empty and 1 means not empty, and integer n
Return if n new flowers can be planted

```txt
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

## Solution

```py
def canPlaceFlowers(self, A, N):
  for i, x in enumerate(A):
    if not x and (i == 0 or A[i-1] == 0) and (i == len(A) - 1 or A[i+1] == 0):
      N -= 1
      A[i] = 1
  return N <= 0
```
