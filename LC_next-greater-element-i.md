{% tabs %}{% tab title='LC_496.py' %}

```py
class Solution:
  def nextGreaterElement(self, findNums, nums):
    st, d = [], {}
    for n in nums:
      while st and st[-1] < n:
        d[st.pop()] = n
      st.append(n)
    return [d.get(x, -1) for x in findNums]
```

{% endtab %}{% endtabs %}