# [LC_three-equal-parts](https://leetcode.com/problems/three-equal-parts)

* en

  ```en
  Given an array arr which consists of only zeros and ones
  Divide the array into three non-empty parts such that all of these parts represent the same binary value
  If it is possible, return any [i, j] with i + 1 < j, such that:
    arr[0], arr[1], ..., arr[i] is the first part,
    arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
    arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part
    All three parts have equal binary values
  If it is not possible, return [-1, -1]
  ```

* tc

  ```tc
  Input: arr = [1,0,1,0,1]
  Output: [0,3]
  ```

## Solution

* py

  ```py
  def threeEqualParts(self, A: List[int]) -> List[int]:
    num_ones = sum(A)
    if num_ones == 0:
      return [0, 2]
    if num_ones % 3 != 0:
      return [-1, -1]

    c = 0
    s1 = s2 = s3 = -1
    for idx,x in enumerate(A): # Find the first 1 in each part
      if x == 1:
        c += 1
      if c == 1 and s1 < 0:
        s1 = idx
      if c == num_ones // 3 + 1 and s2 < 0:
        s2 = idx
      if c == num_ones * 2 // 3 + 1 and s3 < 0:
        s3 = idx
        break
    n = len(A[s3:]) # length of each part when all the leading 0's are removed
    if A[s1: s1 + n] == A[s2: s2 + n] and A[s2: s2 + n] == A[s3:]:
      return [s1 + n - 1, s2 + n]
    else:
      return [-1, -1]
  ```
