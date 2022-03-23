```cpp
vector<vector<int>> kClosest(vector<vector<int>>& A, int K) {
  nth_element(A.begin(), A.begin() + K, A.end(), [](vector<int>& a, vector<int>& b) {
    return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
  });
  return vector<vector<int>>(A.begin(), A.begin() + K);
}
```

```java
public int[][] kClosest(int[][] points, int K) {
  Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
  return Arrays.copyOfRange(points, 0, K);
}
```

```py
def kClosest(self, points, K):
  return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
```
