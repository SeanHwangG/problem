```cpp
vector<int> v, n;
SparseVector(vector<int> &nums, int i = 0) : n(nums) {
  for_each(begin(n), end(n), [&](int k) { if (k) v.push_back(i); ++i; });
}
int dotProduct(SparseVector& vec, vector<int> res = {}) {
  set_intersection(begin(v), end(v), begin(vec.v), end(vec.v), back_inserter(res));
  return accumulate(begin(res), end(res), 0, [&](int s, int i) { return s + n[i] * vec.n[i]; });
}
```

```py
def __init__(self, A: List[int]):
  self.A = A
def dotProduct(self, other: 'SparseVector') -> int:
  return sum([a * b for a, b in zip(self.A, other.A)])
```
