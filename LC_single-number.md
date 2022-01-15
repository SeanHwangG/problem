{% tabs %}{% tab title='LC_136.cpp' %}

```cpp
int singleNumber(vector<int>& nums) {
  return accumulate(begin(nums), end(nums), 0, bit_xor<int>());
};
```

{% endtab %}{% tab title='LC_136.py' %}

```py
def singleNumber(self, nums: List[int]) -> int:
  return reduce(lambda x, y: x ^ y, nums)
```

{% endtab %}{% endtabs %}
