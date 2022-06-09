# [LC_subsets-ii](https://leetcode.com/problems/subsets-ii)

* en

  ```en
  Given an integer array nums that may contain duplicates, return all possible subsets (the power set)
  ```

* tc

  ```tc
  Input: nums = [1,2,2]
  Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
  ```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
      sort(S.begin(), S.end());
      vector<vector<int>> ret = {{}};
      int size = 0, startIndex = 0;
      for (int i = 0; i < S.size(); i++) {
        startIndex = i >= 1 && S[i] == S[i - 1] ? size : 0;
        size = ret.size();
        for (int j = startIndex; j < size; j++) {
          vector<int> temp = ret[j];
          temp.push_back(S[i]);
          ret.push_back(temp);
        }
      }
      return ret;
    }
  };
  ```

* py

  ```py
  from itertools import compress, product
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    return set(tuple(compress(sorted(nums), bits)) for bits in product(range(2), repeat=len(nums)))
  ```
