```py
def minOperationsToFlip(self, E):
  def dp(beg, end):
    if beg == end: return (int(E[beg]) , 1)
    if E[end] in "01":
      p1, c1 = dp(beg, end - 2)
      p2, c2 = dp(end, end)
      op = E[end - 1]
    else:
      if d[end] == beg: return dp(beg + 1, end - 1)
      p1, c1 = dp(beg, d[end] - 2)
      p2, c2 = dp(d[end], end)
      op = E[d[end] - 1]

    if op == "|":
      c3 = 1 if p1 + p2 == 1 else min(c1, c2) + p1
      return (p1 | p2, c3)
    else:
      c3 = 1 if p1 + p2 == 1 else min(c1, c2) + 1 - p1
      return (p1 & p2, c3)

  stack, d = [], {}
  for i, elem in enumerate(E):
    if elem == "(":
      stack.append(i)
    elif elem == ")":
      last = stack.pop()
      d[i] = last
  return dp(0, len(E) - 1)[1]
```