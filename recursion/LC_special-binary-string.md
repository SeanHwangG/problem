# [LC_special-binary-string](https://leetcode.com/problems/special-binary-string)

Special binary strings are binary strings with the following two properties:
Number of 0's is equal to the number of 1's
Every prefix of the binary string has at least as many 1's as 0's
Given special binary string s
Move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them
2 strs are consecutive if last character of first string is exactly 1 idx before first character of second string
Return lexicographically largest resulting string possible after applying mentioned operations on string

```txt
Input: s = "11011000"
Output: "11100100"  # The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
```

## Solution

```py
def makeLargestSpecial(self, S: str) -> str:
  count, i, res = 0, 0, []
  for j, v in enumerate(S):
    count = count + 1 if v == '1' else count - 1
    if count == 0:
      res.append('1' + self.makeLargestSpecial(S[i + 1: j]) + '0')
      i = j + 1
  return ''.join(sorted(res)[::-1])
```
