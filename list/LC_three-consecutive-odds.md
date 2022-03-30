```cpp
auto three_consecutive_odds(auto const& arr) -> bool {
  auto const max_odds = arr
    | rv::group_by([](auto a, auto b) { return a % 2 == b % 2; })
    | rv::filter([](auto rng) { return rng[0] % 2 == 1; })
    | rv::transform(ranges::distance)
    | hs::maximum();
  return max_odds >= 3;
}
```

```py
def threeConsecutiveOdds(self, arr: List[int]) -> bool:
  return any(1 & a & b & c for a, b, c in zip(arr, arr[1:], arr[2:]))
```
