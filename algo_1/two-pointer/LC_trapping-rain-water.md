# [LC_trapping-rain-water](https://leetcode.com/problems/trapping-rain-water)

* en

  ```en
  Given n non-negative integers representing elevation map where the width of each bar is 1
  Compute how much water it can trap after raining
  ```

* tc

  ```tc
  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  ```

## Solution

* cpp

  ```cpp
  int trap(vector<int>& height) {
    int l = 0, r = height.size() - 1, level = 0, water = 0;
    while (l < r) {
      int lower = height[height[l] < height[r] ? l++ : r--];
      level = max(level, lower);
      water += level - lower;
    }
    return water;
  }
  ```
