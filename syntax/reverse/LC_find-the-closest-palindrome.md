# [LC_find-the-closest-palindrome](https://leetcode.com/problems/find-the-closest-palindrome)

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome
If there is a tie, return the smaller one
Closest is defined as the absolute difference minimized between two integers

```txt
Input: n = "123"
Output: "121"

Input: n = "1"
Output: "0"
```

## Solution

* py

  ```py
  def nearestPalindromic(self, n: str) -> str:
    l = len(n)
    candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))  # with different digits width, must be 10...01 or 9...9
    prefix = int(n[:(l + 1) // 2])  # closest must be in middle digit +1, 0, -1, then flip left to right
    for i in map(str, (prefix - 1, prefix, prefix + 1)):
      candidates.add(i + [i, i[:-1]][l & 1][::-1])
    candidates.discard(n)
    return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
  ```
