# [LC_cracking-the-safe](https://leetcode.com/problems/cracking-the-safe)

```en
Password with sequence of n digits where each digit can be in range [0, k-1]
While entering password, last n digits entered will automatically be matched against password
Return len of password guaranteed to open box at some point of entering it
```

```txt
Input: n = 2, k = 2

n = 1, k = 2
Output:
"01100"  # "01100", "10011", "11001" will be accepted

"10"     # "01" will be accepted
```

## Solution

* py

  ```py
  def crackSafe(self, n: int, k: int) -> str:
    visited = set()
    res = s = '0' * (n - 1)
    while True:
      for i in range(k - 1, -1, -1):
        if (s, i) not in visited:
          res += str(i)
          visited.add((s, i))
          s = (s + str(i))[1:]
          break
      else:
        return res
  ```
