# [LC_sum-of-beauty-of-all-substrings](https://leetcode.com/problems/sum-of-beauty-of-all-substrings)

Beauty of a string is difference in frequencies between most frequent and least frequent characters
Given string s, return sum of beauty of all of its substrings

```txt
Input: s = "aabcb"
Output: 5
```

## Solution

```py
def beautySum(self, s: str) -> int:
  ans = 0
  for i in range(len(s)):
    freq = [0]*26
    for j in range(i, len(s)):
      freq[ord(s[j])-97] += 1
      ans += max(freq) - min(x for x in freq if x)
  return ans
```
