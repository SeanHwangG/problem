# [LC_pancake-sorting](https://leetcode.com/problems/pancake-sorting)

Choose int k where 1 <= k <= arr.length
Reverse sub-array arr[0...k-1] (0-indexed)

```txt
Input: arr = [3,2,4,1]
Output: [4,2,4,3] # k = 4, 2, 4, 3
```

## Solution

* py

  ```py
  def pancakeSort(self, A: List[int]) -> List[int]:
    res = []
    for x in range(len(A), 1, -1):
      i = A.index(x)
      res.extend([i + 1, x])
      A = A[:i:-1] + A[:i]
    return res
  ```
