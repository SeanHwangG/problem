# [LC_digit-count-in-range](https://leetcode.com/problems/digit-count-in-range)

```en
Given a single-digit integer d and two integers low and high
Return number of times that d occurs as a digit in all integers in inclusive range [low, right]
```

```txt
Input: d = 3, low = 100, high = 250
Output: 35
```

## Solution

* py

  ```py
  def digitsCount(self, d: int, low: int, high: int) -> int:
    def count(N):
      if N == 0 or d == 0 and N <= 10: return 0
      res = 0
      if N % 10 > d: res += 1
      if N / 10 > 0: res += str(N // 10).count(str(d)) * (N % 10)
      res += N // 10 if d else N // 10 - 1
      res += count(N // 10) * 10
      return res
    return count(high + 1) - count(low)
  ```
