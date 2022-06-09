# [KT_electricaloutlets](https://open.kattis.com/problems/electricaloutlets)

* en

  ```en
  For N lines, find maximum number of plugs with n plugs with port
  ```

* tc

  ```tc
  Input: 3  # N
  3 2 3 4
  10 4 4 4 4 4 4 4 4 4 4
  4 10 10 10 10

  Output: 7 (2 + 1 + 2 + 4)
  31
  37
  ```

## Solution

* py

  ```py
  for _ in range(int(input())):
    li = list(map(int, input().split()))
    count = sum(li) - 2 * li[0] + 1
    print(count)
  ```
