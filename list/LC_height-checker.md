```cpp
int heightChecker(vector<int>& h) {
  auto t = h;
  sort(t.begin(), t.end());
  return inner_product(h.begin(), h.end(), t.begin(), 0, plus<>(), not_equal_to<>());
}
```

```py
def heightChecker(self, heights: List[int]) -> int:
    return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
```
