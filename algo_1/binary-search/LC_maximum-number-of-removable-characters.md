# [LC_maximum-number-of-removable-characters](https://leetcode.com/problems/maximum-number-of-removable-characters)

* en

  ```en
  Given strings s and p where p is a subsequence of s
  Given a distinct integer array removable containing a subset of indices of s
  Return the maximum k you can choose such that p is still a subsequence of s after the removals
  ```

* tc

  ```tc
  Input_1: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
  Output_1: 1

  Input_2: s = "abcab", p = "abc", removable = [0,1,2,3,4]
  Output_2: 0
  ```

## Solution

* cpp

  ```cpp
  int maximumRemovals(string s, string p, vector<int>& rem) {
    int l = 0, r = rem.size();
    while (l < r) {
      int m = (l + r + 1) / 2, j = 0;
      unordered_set<int> st(begin(rem), begin(rem) + m);
      for (int i = 0; i < s.size() && j < p.size(); ++i)
        if (st.count(i) == 0 && s[i] == p[j])
          ++j;
      if (j == p.size())
        l = m;
      else
        r = m - 1;
    }
    return l;
  }
  ```
