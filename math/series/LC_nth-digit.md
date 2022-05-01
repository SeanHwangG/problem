# [LC_nth-digit](https://leetcode.com/problems/nth-digit)

Find nth digit of the infinite integer sequence 1,2,..

```txt
Input: n = 11
Output: 0
```

## Solution

* py

  ```py
  def findNthDigit(self, n):
    n -= 1
    for digits in range(1, 11):
      first = 10**(digits - 1)
      if n < 9 * first * digits:
        return int(str(first + n/digits)[n % digits])
      n -= 9 * first * digits
  ```
