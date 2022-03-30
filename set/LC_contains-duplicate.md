# [LC_contains-duplicate](https://leetcode.com/problems/contains-duplicate)

Check whether list has duplicates in it

```txt
Input: nums = [1,2,3,4]
Output: false
```

## Solution

```go
func containsDuplicate(nums []int) bool {
  m := make(map[int]bool)
  for _, v := range nums {
    if _, ok := m[v]; ok {
      return true
    }
    m[v] = true
  }
  return false
}
```

```js
var containsDuplicate = function(nums) {
  return new Set(nums).size < nums.length;
};
```

```py
def containsDuplicate(self, nums):
  return len(nums) != len(set(nums))
```
