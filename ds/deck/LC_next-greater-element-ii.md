# [LC_next-greater-element-ii](https://leetcode.com/problems/next-greater-element-ii)

* en

  ```en
  Return next greater number for every element in nums
  ```

* tc

  ```tc
  Input: nums = [1,2,1]
  Output: [2,-1,2]
  ```

## Solution

* py

  ```py
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    stack, res = [], [-1] * len(A)
    for i in range(len(A)) * 2:
      while stack and (A[stack[-1]] < A[i]):
        res[stack.pop()] = A[i]
      stack.append(i)
    return res
  ```
