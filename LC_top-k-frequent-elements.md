{% tabs %}{% tab title='LC_347.cpp' %}

```cpp
int maxChunksToSorted(vector<int>& arr) {
  long int sum1 = 0, sum2 = 0, ans = 0;
  vector<int> t = arr;
  sort(t.begin(), t.end());
  for (int i = 0; i < arr.size(); i++) {
    sum1 += t[i];
    sum2 += arr[i];
    if (sum1 == sum2) ans++;
  }
  return int(ans);
}
```

{% endtab %}{% tab title='LC_347.py' %}

```py
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  co = Counter(nums)
  return [a for a, b in co.most_common(k)]
```

{% endtab %}{% endtabs %}
