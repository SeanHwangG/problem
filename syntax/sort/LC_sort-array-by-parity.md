# [LC_sort-array-by-parity](https://leetcode.com/problems/sort-array-by-parity)

```en
Given int array nums, move all even ints at the beginning of array followed by all odd int
Return any array that satisfies this condition.

```

```txt
Input: nums = [3,1,2,4]
Output: [2,4,3,1]  # [4,2,3,1], [2,4,1,3], [4,2,1,3] would also be accepted.

Input: nums = [0]
Output: [0]
```

## Solution

* cpp

  ```cpp
  vector<int> sortArrayByParity(vector<int>& A) {
    partition(A.begin (), A.end (), [](auto e) { return e % 2 == 0; });
  return A;
  }
  ```

* java

  ```java
  public int[] sortArrayByParity(int[] A) {
    for (int i = 0, j = 0; j < A.length; j++)
      if (A[j] % 2 == 0) {
        int tmp = A[i];
        A[i++] = A[j];
        A[j] = tmp;;
      }
    return A;
  }
  ```

* py

  ```py
  def sortArrayByParity(self, A):
    return sorted(A, key=lambda x: x % 2)
  ```
