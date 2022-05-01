# [LC_two-sum](https://leetcode.com/problems/two-sum)

Find two index that sums up to target

```txt
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

## Solution

* go

  ```go
  func twoSum(nums []int, target int) []int {
    m := make(map[int]int, len(nums))

    for i, num := range nums {
      if idx, ok := m[target - num]; ok {
        return []int{idx, i}
      }
      m[num] = i
    }
    return []int{0, 0}
  }
  ```

* java

  ```java
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++){
      if (map.containsKey(target - nums[i]))
        return new int[] { map.get(target - nums[i]), i };
      map.put(nums[i], i);
    }
    return null;
  }
  ```

* py

  ```py
  def twoSum(self, nums, target):
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return d[target - num], i
      d[num] = i
  ```
