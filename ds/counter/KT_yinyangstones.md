# [KT_yinyangstones](https://open.kattis.com/problems/yinyangstones)



```txt
Input: WWBWBB
Output: 1
```

## Solution

* py

  ```py
  from collections import Counter
  cnt = Counter(input())
  print(1 if cnt['W'] == cnt['B'] else 0)
  ```
