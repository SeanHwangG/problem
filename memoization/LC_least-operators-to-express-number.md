```py
def leastOpsExpressTarget(self, x: int, target: int) -> int:
  @lru_cache(None)
  def dp(target, i):
    if target == 1: return 1
    if i == 0: return target + (target - 1)
    count, remainder = target // (x ** i), target % (x ** i)
    if remainder == 0: return count * i - 1
    case1 = i * count + dp(remainder, i - 1)
    case2 = i * (count + 1) + dp(x ** i - remainder, i - 1)
    return min(case1, case2)

  return dp(target, math.ceil(math.log(target, x)))
```