{% tabs %}{% tab title='LC_31.cpp' %}

```cpp
void nextPermutation(vector<int>& nums) {
  next_permutation(begin(nums), end(nums));
}
```

{% endtab %}{% tab title='LC_31.py' %}

```py
def nextPermutation(self, nums):
  i = j = len(nums)-1   # 1: find sorted until
  while i > 0 and nums[i-1] >= nums[i]:
    i -= 1
  if i == 0:
    nums.reverse()
    return
  k = i - 1  # find the last "ascending" position
  while nums[j] <= nums[k]:
    j -= 1
  nums[k], nums[j] = nums[j], nums[k]
  l, r = k+1, len(nums)-1  # reverse the second part
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l +=1 ; r -= 1
```

{% endtab %}{% endtabs %}
