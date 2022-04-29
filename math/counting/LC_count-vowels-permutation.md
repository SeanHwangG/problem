# [LC_count-vowels-permutation](https://leetcode.com/problems/count-vowels-permutation)

Input: n = 2
Output: 10  # "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

```txt
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
```

## Solution

```py
def count_vowel_permutations(n):
  a, e, i, o, u = 1, 1, 1, 1, 1
  for _ in range(n - 1):
    a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
  return (a + e + i + o + u) % (10**9 + 7)
```
