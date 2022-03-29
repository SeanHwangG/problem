* w[i] = stones[i] (Weight of jewel)
* v[i] = stones[i] (Value of jewel)
* W = sum(stones) / 2 (Capacity of bag)

```py
def lastStoneWeightII(self, A):
  dp = {0}  # record achievable sum of smaller group
  for a in A:
    dp |= {a + i for i in dp}
  return min(abs(sum(A) - i - i) for i in dp)
```
