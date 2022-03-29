```cpp
class Solution {
public:
  vector<int> singleNumber(vector<int>& nums) {
    int xored = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
    xored &= -xored;
    vector<int> ret = {0, 0};
    for (int num : nums){
      if (xored & num) ret[0] ^= num;
      else             ret[1] ^= num;
    }
    return ret;
  }
};
```
