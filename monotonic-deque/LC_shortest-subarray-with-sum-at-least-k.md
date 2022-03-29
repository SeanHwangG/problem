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
