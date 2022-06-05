# [LC_consecutive-characters](https://leetcode.com/problems/consecutive-characters)

```en

```

```txt
Input: s = "leetcode"
Output: 2  # Substring "ee" is of length 2 with the character 'e' only.

Input: s = "abbcccddddeeeeedcba"
Output: 5  # Substring "eeeee" is of length 5 with the character 'e' only
```

## Solution

* py

  ```py
  def maxPower(self, s):
    return max(len(list(b)) for a, b in itertools.groupby(s))
  ```
