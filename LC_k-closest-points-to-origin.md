{% tabs %}{% tab title='LC_973.md' %}

* Given an array of points where points[i] = [xi, yi] represents a point on X-Y plane and an integer k
* return k closest points to the origin (0, 0) in any order (guaranteed to be unique)

{% endtab %}{% tab title='LC_973.cpp' %}

```cpp
vector<vector<int>> kClosest(vector<vector<int>>& A, int K) {
  nth_element(A.begin(), A.begin() + K, A.end(), [](vector<int>& a, vector<int>& b) {
    return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
  });
  return vector<vector<int>>(A.begin(), A.begin() + K);
}
```

{% endtab %}{% tab title='LC_973.java' %}

```java
public int[][] kClosest(int[][] points, int K) {
  Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
  return Arrays.copyOfRange(points, 0, K);
}
```

{% endtab %}{% tab title='LC_973.py' %}

```py
def kClosest(self, points, K):
  return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
```

{% endtab %}{% endtabs %}
