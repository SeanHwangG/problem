# [LC_sliding-window-median](https://leetcode.com/problems/sliding-window-median)

Given an integer array nums and an integer k
There is a sliding window of size k which is moving from the very left of the array to the very right
Only see the k numbers in the window, each time the sliding window moves right by one position.
Return median array for each window in the original array (error within 10^-5 will be accepted)

```txt
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
```

## Solution

* cpp

```cpp
vector<double> medianSlidingWindow(vector<int>& nums, int k) {
  multiset<int> window(nums.begin(), nums.begin() + k);
  auto mid = next(window.begin(), k / 2);
  vector<double> medians;
  for (int i = k;; i++) {
    // Push the current median
    medians.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2);

    if (i == nums.size())
      return medians;

    // Insert nums[i]
    window.insert(nums[i]);
    if (nums[i] < *mid) mid--;

    // Erase nums[i - k]
    if (nums[i - k] <= *mid) mid++;
    window.erase(window.lower_bound(nums[i - k]));
  }
}
```

* py

```py
from sortedcontainers import SortedList
class Solution:
  def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    window = SortedList(nums[:k-1])
    median = []

    for a, b in zip(nums, nums[k-1:]):
      window.add(b)
      median.append((window[k // 2] + window[~k // 2]) / 2)
      window.remove(a)

    return median
```
