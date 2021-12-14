{% tabs %}{% tab title='LC_480.cpp' %}

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

{% endtab %}{% tab title='LC_480.py' %}

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

{% endtab %}{% endtabs %}
