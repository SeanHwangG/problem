# [LC_find-the-longest-valid-obstacle-course-at-each-position](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position)

* en

  ```en
  Given integer array, find longest increasing subsequence ends at particular index
  ```

* tc

  ```tc
  Input: obstacles = [1,2,3,2]
  Output: [1,2,3,3]

  Input: obstacles = [3,1,5,6,4,2]
  Output: [1,1,2,3,2,2]
  ```

## Solution

* py

  ```py
  def longestObstacleCourseAtEachPosition(self, A):
    mono, res = [], []
    for a in A:
      i = bisect.bisect(mono, a)
      res.append(i + 1)
      if i == len(mono):
        mono.append(0)
      mono[i] = a
    return res
  ```
