```cpp
int singleNumber(vector<int>& nums) {
  return accumulate(begin(nums), end(nums), 0, bit_xor<int>());
};
```

```py
def singleNumber(self, nums: List[int]) -> int:
  return reduce(lambda x, y: x ^ y, nums)
```
