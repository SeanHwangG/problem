* Time: O(N)

```go
func repeatedNTimes(A []int) int {
  for i := 2; i < len(A); i++ {
    if A[i] == A[i-1] || A[i] == A[i-2] {
      return A[i]
    }
  }
  return A[0]
}
```

* Time: O(1)

```py
def repeatedNTimes(self, A):
  while 1:
    s = random.sample(A, 2)
    if s[0] == s[1]:
      return s[0]
```
