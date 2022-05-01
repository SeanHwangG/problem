# [KT_jobexpenses](https://open.kattis.com/problems/jobexpenses)



```txt
Input: 3
1 -2 3

Output: 2
```

## Solution

* py

  ```py
  print(sum(n for n in map(int, input().split()) if n < 0))
  ```
