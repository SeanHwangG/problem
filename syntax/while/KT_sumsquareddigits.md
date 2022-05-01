# [KT_sumsquareddigits](https://open.kattis.com/problems/sumsquareddigits)



```txt
Input: 3
1 10 1234
2 3 98765
3 16 987654321
Output:
1 30
2 19
3 696
```

## Solution

* py

  ```py
  n_test = int(input())
  def SSD(b, n):
    ret = 0
    while n != 0:
      ret += (n % b) ** 2
      n //= b
    return ret
  for _ in range(1, n_test + 1):
    K, b, n = map(int, input().split())
    print(f'{K} {SSD(b, n)}')
  ```
