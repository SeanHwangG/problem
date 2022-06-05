# [LC_how-many-numbers-are-smaller-than-the-current-number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)

```en
Find sum of all number smaller than current
```

```txt
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
```

## Solution

* py

  ```py
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    return [sum(m < n for m in nums) for n in nums]
  ```
