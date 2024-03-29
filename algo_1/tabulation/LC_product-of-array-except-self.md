# [LC_product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self)

* en

  ```en
  Given int array nums, return an array answer such that answer[i] is equal to product of all nums except nums[i]
  Product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
  ```

* tc

  ```tc
  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
  ```

## Solution

* cpp

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
