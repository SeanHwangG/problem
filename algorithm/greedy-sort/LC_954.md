{% tabs %}{% tab title='LC_954.md' %}

* Given an integer array of even length arr
* Return if we can reorder arr ST arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2

```txt
Input: arr = [2,1,2,6]
Output: false

Input: arr = [4,-2,2,-4]
Output: true
```

{% endtab %}{% tab title='LC_954.py' %}

```py
def canReorderDoubled(self, arr: List[int]) -> bool:
  cnt = Counter(arr)
  for num in sorted(arr, key = lambda x: abs(x)):
    if cnt[num] == 0:
      continue
    if cnt[2 * num] == 0:
      return False
    cnt[num] -= 1
    cnt[2 * num] -= 1
  return True
```

{% endtab %}{% endtabs %}
