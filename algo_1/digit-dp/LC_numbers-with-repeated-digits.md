# [LC_numbers-with-repeated-digits](https://leetcode.com/problems/numbers-with-repeated-digits)

* en

  ```en
  Given a positive integer N, return # positive integers less than or equal to N that have at least 1 repeated digit
  ```

* tc

  ```tc
  Input: 20
  Output: 1
  ```

## Solution

* py

  ```py
  # Count res the Number Without Repeated Digit
  # Transform N + 1 to List
  # Count the number with digits < n
  # Count the number with same prefix
  # Time. O(logN)
  # XXX
  # XX
  # X
  # 1XXX ~ 7XXX
  # 80XX ~ 86XX
  # 870X ~ 875X
  # 8760 ~ 8765
  def numDupDigitsAtMostN(self, N):
    L = list(map(int, str(N + 1)))
    res = 0

    for i in range(1, len(L)): res += 9 * math.perm(9, i - 1) # count postive number with digits less than K
    s = set()
    for i, x in enumerate(L):
      for y in range(0 if i else 1, x):
        if y not in s:
          res += math.perm(9 - i, len(L) - i - 1)
      if x in s: break
      s.add(x)
    return N - res
  ```
