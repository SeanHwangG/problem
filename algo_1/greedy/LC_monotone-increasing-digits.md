# [LC_monotone-increasing-digits](https://leetcode.com/problems/monotone-increasing-digits)

* en

  ```en
  Print largest monotonic increasing number less than N
  ```

* tc

  ```tc
  Input: n = 5432
  Output: 4999
  ```

## Solution

* Find first decreasing digit
* 20s / 5422 -> 300s / 5322 -> 4000s / 4322 -> 4999

* py

  ```py
  def monotoneIncreasingDigits(self, N: int) -> int:
    s = list(str(N))
    maker = len(s)
    for i in range(len(s) - 1, 0, -1):
      if s[i] < s[i - 1]:
        maker = i
        s[i - 1] = str(int(s[i - 1]) - 1)
    s[maker:] = ['9'] * (len(s) - maker)
    return int(''.join(s))
  ```
