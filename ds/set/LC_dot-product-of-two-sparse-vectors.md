# [LC_dot-product-of-two-sparse-vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors)

* en

  ```en
  Implement class SparseVector:
  SparseVector(nums) Initializes the object with the vector nums
  dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
  ```

* tc

  ```tc
  Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
  Output: 8  # v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
  ```

## Solution

* cpp

  ```cpp
  vector<int> v, n;
  SparseVector(vector<int> &nums, int i = 0) : n(nums) {
    for_each(begin(n), end(n), [&](int k) { if (k) v.push_back(i); ++i; });
  }
  int dotProduct(SparseVector& vec, vector<int> res = {}) {
    set_intersection(begin(v), end(v), begin(vec.v), end(vec.v), back_inserter(res));
    return accumulate(begin(res), end(res), 0, [&](int s, int i) { return s + n[i] * vec.n[i]; });
  }
  ```

* py

  ```py
  def __init__(self, A: List[int]):
    self.A = A
  def dotProduct(self, other: 'SparseVector') -> int:
    return sum([a * b for a, b in zip(self.A, other.A)])
  ```
