# [LC_maximum-distance-between-a-pair-of-values](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values)

Given 2 non-increasing 0-indexed integer arrays nums1 and nums2
Pair (i, j), where 0 <= i < nums1.length, 0 <= j < nums2.length, is valid if i<=j, nums1[i]<=nums2[j]
Return maximum (j - i) of any valid pair (i, j). If there are no valid pairs, return 0

```txt
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
```

## Solution

* cpp

  ```cpp
  int maxDistance(vector<int>& A, vector<int>& B) {
    int i = 0, j = 0, res = 0, n = A.size(), m = B.size();
    while (i < n && j < m) {
      if (A[i] > B[j])
        i++;
      else
        res = max(res, j++ - i);
    }
    return res;
  }
  ```
