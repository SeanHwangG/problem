# [LC_minimum-number-of-operations-to-make-string-sorted](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted)

What is the lexicographical order of string

```txt
Input: s = "cba"
Output: 5
```

## Solution

* py

  ```py
  cnt, ans, cur = [0] * 26, 0, 1  # cur: #op for cur positions
  for i, cur_letter in enumerate(s[::-1]):
    num = ord(cur_letter) - ord('a')
    cnt[num] += 1
    cur = cur * (i + 1) // cnt[num]
    ans += cur * sum(cnt[:num]) // (i + 1) # Add number of combinations for all smaller letters than current
  return ans % 1000000007
  ```
