{% tabs %}{% tab title='LC_78.md' %}

* Given an integer array nums of unique elements, return all possible subsets (the power set)

```txt
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

{% endtab %}{% tab title='LC_78.cpp' %}

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

{% endtab %}{% tab title='LC_78.py' %}

```py
def subsets(self, nums):
  return [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
```

{% endtab %}{% endtabs %}
