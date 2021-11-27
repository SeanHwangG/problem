{% tabs %}{% tab title='LC_1063.md' %}

* Given an integer array nums
* Return # of non-empty subarrays with leftmost element of the subarray not larger than other elements in subarray

```txt
Input: nums = [1,4,2,5,3]
Output: 11

Input: nums = [3,2,1]
Output: 3
```

{% endtab %}{% tab title='LC_1063.py' %}

```py
def validSubarrays(self, nums: List[int]) -> int:
  nums.append(-inf)
  stack, result = [], 0
  for i, num in enumerate(nums):
    while stack and nums[stack[-1]] > num:
      result += i - stack.pop()
    stack.append(i)

  return result
```

{% endtab %}{% endtabs %}
