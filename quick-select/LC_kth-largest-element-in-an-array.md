```cpp
int findKthLargest(vector<int>& nums, int k) {
  nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
  return nums[k - 1];
}
```

* Time: O(N)

```py
def findKthLargest(self, li, k):
  pivot = random.choice(li)
  lo  = [l for l in li if l < pivot]
  mi = [e for e in li if e == pivot]
  hi = [r for r in li if r > pivot]
  if k <= len(hi):
    return self.findKthLargest(hi, k)
  elif (k - len(hi)) <= len(mi):
    return mi[0]
  else:
    return self.findKthLargest(lo, k - len(hi) - len(mi))
```
