# [LC_4sum-ii](https://leetcode.com/problems/4sum-ii)

* en

  ```en
  Given four lists A, B, C, D of integer values
  compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
  ```

* tc

  ```tc
  Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
  Output: 2
  ```

## Solution

* cpp

  ```cpp
  int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    int res = 0;
    unordered_map<int, int> AB;
    for (int a : A)
      for (int b : B)
        AB[a + b]++;
    for (int c : C)
      for (int d : D)
        res += AB[-c - d];
    return res;
  }
  ```

* py

  ```py
  def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
  ```
