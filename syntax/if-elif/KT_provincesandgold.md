# [KT_provincesandgold](https://open.kattis.com/problems/provincesandgold)



```txt
Input: 2 1 0
Output: Province or Gold
```

## Solution

* py

  ```py
  g, s, c = map(int, input().split())
  tot = g * 3 + s * 2 + c
  if tot >= 8:
    print("Province or Gold")
  elif tot >= 6:
    print("Duchy or Gold")
  elif tot >= 5:
    print("Duchy or Silver")
  elif tot >= 3:
    print("Estate or Silver")
  elif tot >= 2:
    print("Estate or Copper")
  else:
    print("Copper")
  ```
