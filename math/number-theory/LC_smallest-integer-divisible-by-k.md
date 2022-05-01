# [LC_smallest-integer-divisible-by-k](https://leetcode.com/problems/smallest-integer-divisible-by-k)

Given positive integer K, you need to find the length of the smallest positive integer N
that N is divisible by K, and N only contains the digit 1

```txt
Input: k = 3
Output: 3  # The smallest answer is n = 111, which has length 3
```

## Solution

* py

  ```py
  def smallestRepunitDivByK(self, K: int) -> int:
    if K % 10 not in {1, 3, 7, 9}: return -1
    mod, mod_set = 0, set()
    for length in range(1, K + 1):
      mod = (10 * mod + 1) % K
      if mod == 0: return length
      if mod in mod_set: return -1
      mod_set.add(mod)
    return -1
  ```
