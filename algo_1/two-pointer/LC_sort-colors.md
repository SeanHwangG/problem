# [LC_sort-colors](https://leetcode.com/problems/sort-colors)

* en

  ```en
  Sort three number
  ```

* tc

  ```tc
  Input: nums = [2,0,2,1,1,0]
  Output: [0,0,1,1,2,2]
  ```

## Solution

* py

  ```py
  def sortColors(self, nums):
    red, white, blue = 0, 0, len(nums)-1

    while white <= blue:
      if nums[white] == 0:
        nums[red], nums[white] = nums[white], nums[red]
        white += 1
        red += 1
      elif nums[white] == 1:
        white += 1
      else:
        nums[white], nums[blue] = nums[blue], nums[white]
        blue -= 1
  ```
