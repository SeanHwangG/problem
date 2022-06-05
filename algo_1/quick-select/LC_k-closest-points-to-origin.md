# [LC_k-closest-points-to-origin](https://leetcode.com/problems/k-closest-points-to-origin)

```en
Given array of points where points[i] = [xi, yi] represents a point on X-Y plane and an integer k
return k closest points to the origin (0, 0) in any order (guaranteed to be unique)
```

```txt
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

## Solution

* cpp

  ```cpp
  vector<vector<int>> kClosest(vector<vector<int>>& A, int K) {
    nth_element(A.begin(), A.begin() + K, A.end(), [](vector<int>& a, vector<int>& b) {
      return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
    });
    return vector<vector<int>>(A.begin(), A.begin() + K);
  }
  ```

* java

  ```java
  public int[][] kClosest(int[][] points, int K) {
    Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
    return Arrays.copyOfRange(points, 0, K);
  }
  ```

* py

  ```py
  def kClosest(self, points, K):
    return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
  ```
