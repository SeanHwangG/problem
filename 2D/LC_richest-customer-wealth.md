```cpp
auto maximumWealth(auto const& accounts) -> int {
  return std::ranges::max(accounts | std::views::transform([](auto const& row) {
    return std::reduce(row.cbegin(), row.cend());
  }));
}
```

```py
return max(map(sum, accounts))
```
