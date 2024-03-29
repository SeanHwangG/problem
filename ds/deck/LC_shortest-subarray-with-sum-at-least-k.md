# [LC_shortest-subarray-with-sum-at-least-k](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

* en

  ```en
  Return length of shortest, non-empty, contiguous subarray of nums with sum at least k
  If there is no non-empty subarray with sum at least k, return -1
  ```

* tc

  ```tc
  Input: nums = [2,-1,2], k = 3
  Output: 3
  ```

## Solution

* py

  ```py
  def shortestSubarray(self, A: List[int], k: int) -> int:
    dq = collections.deque([])
    B = [0]
    for a in A:
      B.append(B[-1] + a)

    res = float('inf')
    for i, b in enumerate(B):
      if not dq: dq.append(i)
      else:
        while dq and B[dq[-1]] > b: dq.pop()
        while dq and B[dq[0]] <= b - k:
          res = min(res, i - dq[0])
          dq.popleft()
        dq.append(i)
    return res if res < float('inf') else -1
  ```
