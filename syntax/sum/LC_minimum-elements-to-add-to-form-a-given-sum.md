# [LC_minimum-elements-to-add-to-form-a-given-sum](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum)

Given int array nums and two integers limit and goal. abs(nums[i]) <= limit
Return the minimum number of elements you need to add to make the sum of the array equal to goal
The array must maintain its property that abs(nums[i]) <= limit

```txt
Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2  # add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4
```

## Solution

* py

```py
def minElements(self, A, limit, goal):
  return (abs(sum(A) - goal) + limit - 1) / limit
```
