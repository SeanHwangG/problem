# [KT_sevenwonders](https://open.kattis.com/problems/sevenwonders)



```txt
Input: TCGTTC
Output: 21
```

## Solution

```py
from collections import Counter
st = input()
co = Counter(st)
ret = min(co['T'], co['C'], co['G']) * 7
ret += co['T'] ** 2
ret += co['C'] ** 2
ret += co['G'] ** 2

print(ret)
```
