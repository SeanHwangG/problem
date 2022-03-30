# [LC_combinations](https://leetcode.com/problems/combinations)

Given n, k return all possible combinations of k numbers out of the range (1, n) in any order

```txt
Input: n = 4, k = 2
Output: [[2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],]
```

## Solution

```py
def combine(self, n: int, k: int) -> List[List[int]]:
  if k == 0:
    return [[]]
  return [pre + [i] for i in range(k, n + 1) for pre in self.combine(i - 1, k - 1)]
```
