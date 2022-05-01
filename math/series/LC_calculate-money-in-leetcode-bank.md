# [LC_calculate-money-in-leetcode-bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank)

Hercy puts money in Leetcode bank every day
He starts by putting in $1 on Monday, first day. Every day from Tuesday to Sunday, put in $1 more than day before
On every subsequent Monday, he will put in $1 more than the previous Monday
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day

```txt
Input: n = 10
Output: 37
```

## Solution

* py

  ```py
  def totalMoney(self, n: int) -> int:
    k, r = divmod(n, 7)
    return 28 * k + k * (k - 1) // 2 * 7 + (1 + r) * r // 2 + k * r
  ```
