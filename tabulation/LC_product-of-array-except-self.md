```cpp
vector<int> productExceptSelf(vector<int>& nums) {
  int n = nums.size();
  vector<int> prods(n, 1);
  for (int i = 1; i < n; i++) // product from left
    prods[i] = prods[i - 1] * nums[i - 1];

  for (int j = n - 1, m = 1; j >= 0; j--) {
    prods[j] *= m; // product from right
    m *= nums[j];
  }
  return prods;
}
```
