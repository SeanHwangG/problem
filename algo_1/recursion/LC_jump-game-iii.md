# [LC_jump-game-iii](https://leetcode.com/problems/jump-game-iii)

* en

  ```en
  Initially positioned at start index of the array. When at index i, can jump to i + arr[i] or i - arr[i]
  Check if reach to any index with value 0
  ```

* tc

  ```tc
  Input: arr = [4,2,3,0,3,1,2], start = 5
  Output: true

  Input: arr = [4,2,3,0,3,1,2], start = 0
  Output: true
  ```

## Solution

* cpp

  ```cpp
  bool canReach(vector<int>& A, int i) {
    return 0 <= i && i < A.size() && A[i] >= 0 && (!(A[i] = -A[i]) || canReach(A, i + A[i]) || canReach(A, i - A[i]));
  }
  ```
