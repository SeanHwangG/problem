{% tabs %}{% tab title='LC_905.cpp' %}

```cpp
vector<int> sortArrayByParity(vector<int> &A) {
  for (int i = 0, j = 0; j < A.size(); j++)
    if (A[j] % 2 == 0) swap(A[i++], A[j]);
  return A;
}
```

{% endtab %}{% tab title='LC_905.java' %}

```java
public int[] sortArrayByParity(int[] A) {
  for (int i = 0, j = 0; j < A.length; j++)
    if (A[j] % 2 == 0) {
      int tmp = A[i];
      A[i++] = A[j];
      A[j] = tmp;;
    }
  return A;
}
```

{% endtab %}{% endtabs %}
