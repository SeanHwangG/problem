# [LC_make-array-strictly-increasing](https://leetcode.com/problems/make-array-strictly-increasing)

* en

  ```en
  Given two integer arrays arr1 and arr2, return min # operations (possibly zero) needed to make arr1 strictly increasing
  In one operation, choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do assignment arr1[i] = arr2[j]
  If there is no way to make arr1 strictly increasing, return -1.

  ```

* tc

  ```tc
  Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
  Output: 1  # Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
  ```

## Solution

* py

  ```py
  def makeArrayIncreasing(self, li1: List[int], li2: List[int]) -> int:
    dp = {-1:0}
    li2.sort()
    for i in li1:
      tmp = defaultdict(lambda: float('inf'))
      for key in dp:
        if i > key:
          tmp[i] = min(tmp[i], dp[key])
        loc = bisect_right(li2, key)
        if loc < len(li2):
          tmp[li2[loc]] = min(tmp[li2[loc]], dp[key]+1)
      dp = tmp
    return min(dp.values()) if dp else -1
  ```
