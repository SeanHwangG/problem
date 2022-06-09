# [LC_maximum-subarray-min-product](https://leetcode.com/problems/maximum-subarray-min-product)

* en

  ```en
  Min-product of an array is equal to the minimum value in the array multiplied by the array's sum
  Given array of int nums, return max min-product of any non-empty subarray of nums, modulo 10^9 + 7
  ```

* tc

  ```tc
  Input: nums = [1,2,3,2]
  Output: 14
  ```

## Solution

* cpp

  ```cpp
  int maxSumMinProduct(vector<int>& n) {
    long res = 0;
    vector<long> dp(n.size() + 1), st;
    for (int i = 0; i < n.size(); ++i)
      dp[i + 1] = dp[i] + n[i];
    for (int i = 0; i <= n.size(); ++i) {
      while (!st.empty() && (i == n.size() || n[st.back()] > n[i])) {
        int j = st.back();
        st.pop_back();
        res = max(res, n[j] * (dp[i] - dp[st.empty() ? 0: st.back() + 1]));
      }
      st.push_back(i);
    }
    return res % 1000000007;
  }
  ```
