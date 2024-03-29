# [LC_rotate-image](https://leetcode.com/problems/rotate-image)

* en

  ```en
  Rotate 2D array
  ```

* tc

  ```tc
  Input:
  matrix =
  [[5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]]

  Output:
  [[15,13,2,5],
  [14,3,4,1],
  [12,6,8,9],
  [16,7,10,11]]
  ```

## Solution

* cpp

  ```cpp
  /*
  * clockwise rotate: first reverse up to down, then swap the symmetry
  * 1 2 3     7 8 9     7 4 1
  * 4 5 6  => 4 5 6  => 8 5 2
  * 7 8 9     1 2 3     9 6 3
  */
  void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i)
      for (int j = i + 1; j < matrix[i].size(); ++j)
        swap(matrix[i][j], matrix[j][i]);
  }
  ```

* py

  ```py
  def rotate(self, A):
    A[:] = zip(*A[::-1])
  ```
