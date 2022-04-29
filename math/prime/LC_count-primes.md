# [LC_count-primes](https://leetcode.com/problems/count-primes)

Count # prime numbers less than a non-negative number, n

```txt
Input: n = 10
Output: 4
```

## Solution

* py

```py
def countPrimes(self, n: int) -> int:
  if n < 3: return 0
  primes = [True] * n
  primes[0] = primes[1] = False
  for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
      primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
  return sum(primes)
```
