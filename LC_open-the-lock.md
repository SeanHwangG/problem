```py
def openLock(self, deadends, target):
  dead = set(deadends)
  if "0000" in dead: return -1

  q1, q2 = deque([(0, "0000")]), deque([(0, target)])
  visited1, visited2 = {"0000": 0}, {target: 0}
  limit, ans = float("inf"), float("inf")

  while q1:
    if len(q1) > len(q2):
      q1, q2 = q2, q1
      visited1, visited2 = visited2, visited1

    steps, code = q1.popleft()
    if steps + q2[0][0] > limit: return ans

    if code in visited2:
      limit = steps + q2[0][0]
      ans = min(visited1[code] + visited2[code], ans)

    for i in range(4):
      d = int(code[i])
      for k in (d - 1) % 10, (d + 1) % 10:
        cand = code[:i] + str(k) + code[i+1:]
        if cand not in visited1 and cand not in dead:
          visited1[cand] = steps + 1
          q1.append((steps+1, cand))
  return -1
```
