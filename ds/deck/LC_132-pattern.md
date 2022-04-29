# [LC_132-pattern](https://leetcode.com/problems/132-pattern)

Given array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
ST i < j < k and nums[i] < nums[k] < nums[j]
Return whether there is 132 pattern in the list

```txt
Input: nums = [1,2,3,4]
Output: false
```

## Solution

* cpp

```cpp
bool find132pattern(vector<int>& nums) {
  int s3 = INT_MIN;
  stack<int> st;
  for( int i = nums.size()-1; i >= 0; i -- ){
    if( nums[i] < s3 ) return true;
    else while( !st.empty() && nums[i] > st.top() ){
      s3 = st.top(); st.pop();
    }
    st.push(nums[i]);
  }
  return false;
}
```
