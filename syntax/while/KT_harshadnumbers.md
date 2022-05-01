# [KT_harshadnumbers](https://open.kattis.com/problems/harshadnumbers)



```txt
Input: 25
Output: 27
```

## Solution

* py

  ```py
  def is_harshad(num):
    digit_sum = 0
    cur = num
    while cur != 0:
      digit_sum += cur % 10
      cur //= 10
    return num % digit_sum == 0
  n = int(input())
  while True:
    if is_harshad(n):
      print(n)
      break
    n = n + 1
  ```
