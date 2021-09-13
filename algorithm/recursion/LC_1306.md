{% tabs %}{% tab title='LC_1306.md' %}

* Initially positioned at start index of the array. When at index i, can jump to i + arr[i] or i - arr[i]
* Check if reach to any index with value 0

```txt
Input:
Output:
```

{% endtab %}{% tab title='LC_1306.cpp' %}

```cpp
bool canReach(vector<int>& A, int i) {
  return 0 <= i && i < A.size() && A[i] >= 0 && (!(A[i] = -A[i]) || canReach(A, i + A[i]) || canReach(A, i - A[i]));
}
```

{% endtab %}{% endtabs %}
