{% tabs %}{% tab title='LC_1980.md' %}

* Given array of strings nums containing n unique binary strings with length n
* return any binary string of length n that is not in nums

```txt
Input: nums = ["01","10"]
Output: "11"  # "00" also works

Input: nums = ["00","01"]
Output: "11"

Input: nums = ["111","011","001"]
Output: "101"
```

{% endtab %}{% tab title='LC_1980.py' %}

```py
def findDifferentBinaryString(self, nums: List[str]) -> str:
  return ''.join([str(1 ^ int(num[i])) for i, num in enumerate(nums)])
```

{% endtab %}{% endtabs %}
