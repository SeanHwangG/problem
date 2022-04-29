# [KT_batterup](https://open.kattis.com/problems/batterup)



```txt
Input: 3
3 0 2

Output:
1.6666666666667
```

## Solution

* py

  ```py
  n_hit = int(input())
  li = list(map(int, input().split()))
  miss = li.count(-1)
  print((sum(li) + miss) / (n_hit - miss))
  ```
