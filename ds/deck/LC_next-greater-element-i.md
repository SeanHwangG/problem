# [LC_next-greater-element-i](https://leetcode.com/problems/next-greater-element-i)

* en

  ```en
  Given 2 integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2
  Find all the next greater numbers for nums1's elements in the corresponding places of nums2
  ```

* tc

  ```tc
  Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
  Output: [-1,3,-1]
  ```

## Solution

* py

  ```py
  class Solution:
    def nextGreaterElement(self, findNums, nums):
      st, d = [], {}
      for n in nums:
        while st and st[-1] < n:
          d[st.pop()] = n
        st.append(n)
      return [d.get(x, -1) for x in findNums]
  ```
