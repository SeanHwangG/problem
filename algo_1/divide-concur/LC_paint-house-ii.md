# [LC_paint-house-ii](https://leetcode.com/problems/paint-house-ii)

* en

  ```en
  Given row of n houses, painted with 1 of k colors ST all houses such that no two adjacent houses have the same color
  Cost of painting each house with a certain color is represented by an n x k cost matrix costs
  Return the minimum cost to paint all houses
  ```

* tc

  ```tc
  Input: costs = [[1,5,3],[2,9,4]]
  Output: 5

  Input: costs = [[1,3],[2,4]]
  Output: 5
  ```

## Solution

* py
  * Time; O(NK)

  ```py
  def minCostII(self, costs: List[List[int]]) -> int:
    return min(reduce(lambda x, y: self.combine(y, x), costs)) if costs else 0

  def combine(self, house, tmp):
    m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
    tmp = [m] * i + [min(tmp[0: i] + tmp[i + 1:])] + [m] * (n - i - 1)
    return [sum(i) for i in zip(house, tmp)]
  ```
