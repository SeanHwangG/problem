# [LC_first-missing-positive](https://leetcode.com/problems/first-missing-positive)

* en

  ```en
  Given unsorted integer array nums, find the smallest missing positive integer
  ```

* tc

  ```tc
  Input: nums = [1,2,0]
  Output: 3
  ```

## Solution

* cpp

  ```cpp
  int firstMissingPositive(int A[], int n) {
    for (int i = 0; i < n; ++ i)
      while (A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
        swap(A[i], A[A[i] - 1]); // Put number in its right place

    for(int i = 0; i < n; ++ i)
      if(A[i] != i + 1)
        return i + 1;

    return n + 1;
  }
  ```
