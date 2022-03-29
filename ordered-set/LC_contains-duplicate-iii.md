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
