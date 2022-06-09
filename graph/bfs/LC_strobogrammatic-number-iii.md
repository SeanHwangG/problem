# [LC_strobogrammatic-number-iii](https://leetcode.com/problems/strobogrammatic-number-iii)

* en

  ```en
  Given two strings low and high where low <= high, return # strobogrammatic numbers in range [low, high]
  Strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)
  ```

* tc

  ```tc
  Input: low = "50", high = "100"
  Output: 3  # 88 69 96
  ```

## Solution

* py

  ```py
  def strobogrammaticInRange(self, low: str, high: str) -> int:
    q, cnt, low, high, ln = ["", "0", "1", "8"], 0, int(low), int(high), len(high)
    while q:
      s = q.pop()
      if s and s[0] != "0" and low <= int(s) <= high: cnt += 1
      q += [l + s + r for l, r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0")) if len(s) <= ln - 2]
    return cnt if low != 0 else cnt + 1
  ```
