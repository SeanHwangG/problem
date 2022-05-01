# [LC_contains-duplicate-ii](https://leetcode.com/problems/contains-duplicate-ii)

Given array and integer k
Return if there are two distinct indices i and j in array ST nums[i] == nums[j] and abs(i - j) <= k

```txt
Input: nums = [1,2,3,1], k = 3
Output: true
```

## Solution

* go

  ```go
  func containsNearbyDuplicate(nums []int, k int) bool {
    dic := make(map[int]int, len(nums))
    for i, v := range nums{
      if pos, ok := dic[v]; ok && i - pos <= k {
        return true
      }
      dic[v] = i
    }
    return false
  }
  ```

* py

  ```py
  def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
      if v in dic and i - dic[v] <= k:
        return True
      dic[v] = i
    return False
  ```
