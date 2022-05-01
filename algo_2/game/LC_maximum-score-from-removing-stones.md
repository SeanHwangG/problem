# [LC_maximum-score-from-removing-stones](https://leetcode.com/problems/maximum-score-from-removing-stones)

Begin with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively
Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score
Game stops when there are fewer than two non-empty piles, return maximum score you can get

```txt
Input: a = 2, b = 4, c = 6
Output: 6
```

## Solution

* py

  ```py
  def maximumScore(self, a: int, b: int, c: int) -> int:
    a, b, c = sorted([a, b, c])
    return (a + b + c) // 2 if a + b >= c else a + b
  ```
