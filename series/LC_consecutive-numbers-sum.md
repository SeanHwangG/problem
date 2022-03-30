# [LC_consecutive-numbers-sum](https://leetcode.com/problems/consecutive-numbers-sum)

Given an integer n, return # ways write n as sum of consecutive positive integers

```txt
Input: n = 5
Output: 2  # 5 = 2 + 3

Input: n = 9
Output: 3  # 9 = 4 + 5 = 2 + 3 + 4
```

## Solution

* $$ Σ_{i=2}^{N+1} = Σ_{i=1}^{N} + N $$
* Log(N)

```cpp
int consecutiveNumbersSum(int N, int res = 0) {
  for (auto n = 2; n * (n + 1) / 2 <= N; ++n)
    res += (N - n * (n + 1) / 2) % n == 0? 1 : 0;
  return res + 1;
}
```

* Log(N)

```py
def consecutiveNumbersSum(self, n):
  res = 1
  for i in range(2, math.ceil((1 + (1 + 8 * n) ** 0.5) / 2)):
    if ((n / i) - (i - 1)/2).is_integer():
      res += 1
  return res
```
