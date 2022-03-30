# [HR_matching-word-boundaries](https://www.hackerrank.com/challenges/matching-word-boundaries)

Start with vowel (a,e,i,o, u, A, E, I , O or U)
Any length. The matched word should consist of letters (lowercase and uppercase both) only
Matched word must start and end with a word boundary
  Before the first character in the string, if the first character is a word character
  Between two characters in the string, where one is a word character and the other is not a word character
  After the last character in the string, if the last character is a word character

```txt
Input: Found any match?
Output: true
```

## Solution

```py
import re
pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
print(str(bool(re.search(pattern, input()))).lower())
```
