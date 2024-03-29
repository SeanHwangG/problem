# [LC_kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)

* en

  ```en
  Given n x n matrix where each of rows, columns sorted in ascending order, return kth smallest element
  Note that it is kth smallest element in sorted order, not kth distinct element
  ```

* tc

  ```tc
  Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
  Output: 13
  ```

## Solution

* cpp
  * Time; O(n x log(n) x log(N))
  * Space; O(1)

  ```cpp
  int kthSmallest(vector<vector<int>>& matrix, int k) {
    int n = matrix.size();
    int lo = matrix[0][0], hi = matrix[n-1][n-1];
    while (lo < hi) {
      int mi = (lo + hi) / 2;
      int count = 0;  // number of elements no bigger than mi
      for (int i = 0; i < n; i++) {
        vector<int>& row = matrix[i];
        count += std::upper_bound(row.begin(), row.end(), mi) - row.begin();
      }
      if (count < k)
        lo = mi + 1;
      else
        hi = mi;
    }
    return lo;
  }
  ```

* py
  * Time: O(n * log n)
  * Space: O(1)

  ```py
  def kthSmallest(self, matrix, k):
    return sorted(itertools.chain(*matrix))[k - 1]
  ```
