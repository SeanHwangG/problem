# [LC_ipo](https://leetcode.com/problems/ipo)

* en

  ```en
  Given n projects where ith project has a pure profit profits[i] and min capital of capital[i] is needed to start it
  Starts with w capital. When finish project, obtain its pure profit and profit will be added to your total capital
  Pick at most k distinct projects from given projects to maximize final capital, and return final maximized capital
  ```

* tc

  ```tc
  Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
  Output: 4
  ```

## Solution

* py

  ```py
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    pc = sorted(zip(capital, profits))
    i, heap = 0, []
    for _ in range(k):
      while i < len(pc) and pc[i][0] <= w:
        heapq.heappush(heap, -pc[i][1])
        i += 1
      if not heap: return w
      w -= heapq.heappop(heap)
    return w
  ```
