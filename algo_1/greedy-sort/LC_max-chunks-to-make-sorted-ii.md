# [LC_max-chunks-to-make-sorted-ii](https://leetcode.com/problems/max-chunks-to-make-sorted-ii)

```en
Given int array arr, split arr into some number of chunks (i.e., partitions), and individually sort each chunk
After concatenating them, the result should equal the sorted array
Return largest # chunks we can make to sort the array
```

```txt
Input: arr = [5,4,3,2,1]
Output: 1

Input: arr = [2,1,3,4,4]
Output: 4
```

## Solution

* py

  ```py
  def maxChunksToSorted(self, A):
    res, s1, s2 = 0, 0, 0
    for a, b in zip(A, sorted(A)):
      s1 += a
      s2 += b
      res += s1 == s2
    return res
  ```
