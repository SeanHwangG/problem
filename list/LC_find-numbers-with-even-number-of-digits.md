```cpp
int findNumbers(vector<int>& nums) {
  return accumulate(nums.cbegin(), nums.cend(), 0,
    [](auto a, auto b) {
      return a + (to_string(b).size() % 2 == 0);
    });
}
```

```py
def findNumbers(self, nums: List[int]) -> int:
  return len([i for i in nums if len(str(i)) % 2 == 0])
```
