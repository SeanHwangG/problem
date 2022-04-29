# [KT_acm](https://open.kattis.com/problems/acm)



```txt
Input:
3 E right
10 A wrong
30 C wrong
50 B wrong
100 A wrong
200 A right
250 C wrong
300 D right
-1

Output: 3 543
```

## Solution

* py

```py
from collections import Counter
total_score = total_time = 0
penalty = Counter()
while True:
  st = input()
  if st == '-1':
    break
  t, prob, result = st.split()
  t = int(t)

  if result == 'wrong':
    penalty[prob] += 20
  elif result == 'right':
    total_time += t + penalty[prob]
    total_score += 1

print(total_score, total_time)
```
