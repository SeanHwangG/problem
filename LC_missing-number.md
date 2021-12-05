{% tabs %}{% tab title='LC_268.md' %}

* Given array nums containing n distinct numbers in range [0, n], return only number in range that is missing from array

```txt
Input: nums = [3,0,1]
Output: 2
```

{% endtab %}{% tab title='LC_268.py' %}

```py
def missingNumber(self, nums: List[int]) -> int:
  n = len(nums)
  return n * (n+1) // 2 - sum(nums)
```

{% endtab %}{% endtabs %}
