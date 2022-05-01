# [KT_hangingout](https://open.kattis.com/problems/hangingout)



```txt
Input: 4 5  # L, x
enter 3
enter 2
leave 1
enter 1
enter 2

Output: 2
```

## Solution

* py

  ```py
  max_n, n_line = map(int, input().split())
  cur, ret = 0, 0
  for _ in range(n_line):
    st, n = input().split()
    n = int(n)
    if st == 'enter':
      if n + cur <= max_n:
        cur += n
      else:
        ret += 1
    else:
      cur -= n
  print(ret)
  ```
