```go
func climbStairs(n int) int {
  a := 1
  b := 1
  for ; n > 0; n-- {
    a, b = b, a+b
  }
  return a
}
```

```py
def climbStairs(self, n):
  return int((5 ** .5 / 5) * (((1 + 5 ** .5) / 2) ** (n + 1) - ((1 - 5 ** .5) / 2) ** (n + 1)))
```
