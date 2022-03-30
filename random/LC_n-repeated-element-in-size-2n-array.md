# [LC_n-repeated-element-in-size-2n-array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array)

In array nums of size 2 x n, there are n + 1 unique elements, and exactly one of these elements is repeated n times
Return element repeated n times

```txt
Input: nums[2,1,2,5,3,2]
Output: 2
```

## Solution

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
