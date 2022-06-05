# [LC_contains-duplicate-iii](https://leetcode.com/problems/contains-duplicate-iii)

```en
Given an int array nums and two integers k and t, return if there are two distinct indices i and j in array
Such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k
```

```txt
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

## Solution

* cpp

  ```cpp
  bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    set<long long> window;
    for (int i = 0; i < nums.size(); ++i) {
      if (i > k && i - k - 1 < nums.size()) window.erase(nums[i - k - 1]);
      auto it = window.lower_bound((long long)nums[i] - t);
      if (it != window.cend() && *it - nums[i] <= t) return true;
      window.insert(nums[i]);
    }
    return false;
  }
  ```

* py

  ```py
  from sortedcontainers import SortedList

  def containsNearbyAlmostDuplicate(self, nums, k, t):
      slist = SortedList()
      for i, n in enumerate(nums):
        if i > k: SList.remove(nums[i - k - 1])
        pos1 = SortedList.bisect_left(slist, n - t)
        pos2 = SortedList.bisect_right(slist, n + t)
        if pos1 != pos2 and pos1 != len(slist): return True
        slist.add(n)

      return False
  ```
