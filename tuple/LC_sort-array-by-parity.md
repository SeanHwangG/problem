# [LC_sort-array-by-parity](https://leetcode.com/problems/sort-array-by-parity)

Given array nums of non-negative integers, return an array consisting of all even nums, followed by all odd nums.
return any answer array that satisfies this condition.

```txt
Input: nums = [3,1,2,4]
Output: [2,4,3,1]  # [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

## Solution

```cpp
vector<int> sortArrayByParity(vector<int> &A) {
  for (int i = 0, j = 0; j < A.size(); j++)
    if (A[j] % 2 == 0) swap(A[i++], A[j]);
  return A;
}
```

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
