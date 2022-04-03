# [LC_pizza-with-3n-slices](https://leetcode.com/problems/pizza-with-3n-slices)

There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:
  You will pick any pizza slice
  Your friend Alice will pick next slice in anti clockwise direction of your pick
  Your friend Bob will pick next slice in clockwise direction of your pick
  Repeat until there are no more slices of pizzas
Sizes of Pizza slices is represented by circular array slices in clockwise direction
Return the maximum possible sum of slice sizes which you can have

```txt
Input: slices = [3,1,2]
Output: 3

Input: slices = [1,2,3,4,5,6]
Output: 10
```

## Solution

```py
def maxSizeSlices(self, A):
  @lru_cache(None)
  def dp(i, j, k, cycle=0):
    if k == 1: return max(A[i: j + 1])
    if j - i + 1 < k * 2 - 1: return -float('inf')
    return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))
  return dp(0, len(A) - 1, len(A) // 3, 1)
```
