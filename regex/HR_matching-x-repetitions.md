# [HR_matching-x-repetitions](https://www.hackerrank.com/challenges/matching-x-repetitions)

Must be of length equal to 45
First characters should consist of letters(both lowercase and uppercase), or of even digits
Last characters should consist of odd digits or whitespace characters

```txt
Input: 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
Output: true
```

## Solution

```py
import re
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'  # Do not delete 'r'.
print(str(bool(re.search(pattern, input()))).lower())
```
