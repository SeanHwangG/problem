```cpp
vector<vector<int>> subsets(vector<int>& nums) {
  vector<vector<int>> subs = {{}};
  for (int num : nums) {
    for (int i = 0; i < subs.size(); i++) {
      subs.push_back(subs[i]);
      subs.back().push_back(num);
    }
  }
  return subs;
}
```

```py
def subsets(self, nums):
  return [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
```
