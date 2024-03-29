# [LC_shortest-bridge](https://leetcode.com/problems/shortest-bridge)

* en

  ```en
  In given 2D binary array A, there are 2 islands (4-dir connected group of 1s not connected to any other 1s)
  Now, we may change 0s to 1s so as to connect two islands together to form 1 island
  Return smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1)
  ```

* tc

  ```tc
  Input: A =
  [[1,1,1,1,1],
   [1,0,0,0,1],
   [1,0,1,0,1],
   [1,0,0,0,1],
   [1,1,1,1,1]]
  Output: 1
  ```

## Solution

* cpp

  ```cpp
  int paint(vector<vector<int>>& A, int i, int j) {
    if (i < 0 || j < 0 || i == A.size() || j == A.size() || A[i][j] != 1) return 0;
    A[i][j] = 2;
    return 1 + paint(A, i + 1, j) + paint(A, i - 1, j) + paint(A, i, j + 1) + paint(A, i, j - 1);
  }
  bool expand(vector<vector<int>>& A, int i, int j, int cl) {
    if (i < 0 || j < 0 || i == A.size() || j == A.size()) return false;
    if (A[i][j] == 0) A[i][j] = cl + 1;
    return A[i][j] == 1;
  }
  int shortestBridge(vector<vector<int>>& A) {
    for (int i = 0, found = 0; !found && i < A.size(); ++i)
      for (int j = 0; !found && j < A[0].size(); ++j) found = paint(A, i, j);

    for (int cl = 2;; ++cl)
      for (int i = 0; i < A.size(); ++i)
        for (int j = 0; j < A.size(); ++j)
          if (A[i][j] == cl && ((expand(A, i - 1, j, cl) || expand(A, i, j - 1, cl) || expand(A, i + 1, j, cl) \
                              || expand(A, i, j + 1, cl))))
              return cl - 2;
  }
  ```
