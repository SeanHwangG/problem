# [LC_last-stone-weight-ii](https://leetcode.com/problems/last-stone-weight-ii)

```en
Given an array of integers stones where stones[i] is weight of ith stone
On each turn, choose any two stones with x, y (x <= y) and smash them together
  If x == y, both stones are destroyed, and
  If x != y, stone of weight x is destroyed, and stone of weight y has new weight y - x
Return smallest possible weight of left stone at end. if no stones left, 0
```

```txt
Input: stones = [2,7,4,1,8,1]
Output: 1

Input: stones = [1,2]
Output: 1
```

## Solution

* w[i] = stones[i] (Weight of jewel)
* v[i] = stones[i] (Value of jewel)
* W = sum(stones) / 2 (Capacity of bag)

* py

  ```py
  def lastStoneWeightII(self, A):
    dp = {0}  # record achievable sum of smaller group
    for a in A:
      dp |= {a + i for i in dp}
    return min(abs(sum(A) - i - i) for i in dp)
  ```
