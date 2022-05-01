# [LC_pairs-of-songs-with-total-durations-divisible-by-60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60)

Number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0

```txt
Input: time = [30,20,150,100,40]
Output: 3
```

## Solution

* py

  ```py
  def numPairsDivisibleBy60(self, time):
    c = [0] * 60
    res = 0
    for t in time:
      res += c[-t % 60]
      c[t % 60] += 1
    return res
  ```
