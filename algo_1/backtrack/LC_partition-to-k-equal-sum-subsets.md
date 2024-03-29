# [LC_partition-to-k-equal-sum-subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)

* en

  ```en
  Given int array nums and int k, return if can divide array into k non-empty subsets whose sums are all equal
  ```

* tc

  ```tc
  Input: nums = [4,3,2,3,5,2,1], k = 4
  Output: true  # 5, 1 4, 2 3, 2 3
  ```

## Solution

* cpp

  ```cpp
  // Time; O(k * 2^n)
  bool recur(vector<int>& subset, vector<int>& nums, int index, int sum){
    if (index == nums.size()) return true;
    for (int i = 0; i < subset.size(); i++){
    while (i != subset.size() - 1 && subset[i] == subset[i + 1]) i++;
    subset[i] += nums[index];
    if (subset[i] <= sum && recur(subset, nums, index + 1, sum))  return true;
    subset[i] -= nums[index];
    }
    return false;
  }
  bool canPartitionKSubsets(vector<int>& nums, int k) {
    vector<int> subset(k, 0);
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % k != 0)   return false;
    sort(nums.rbegin(), nums.rend());
    return recur(subset, nums, 0, sum / k);
  }
  ```

* py

  ```py
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    sums = [0] * k
    subsum = sum(nums) // k
    nums.sort(reverse=True)

    def backtrack(i):
      if i == len(nums):
        return len(set(sums)) == 1
      for j in range(k):
        sums[j] += nums[i]
        if sums[j] <= subsum and backtrack(i+1):
          return True
        sums[j] -= nums[i]
        if sums[j] == 0:
          break
      return False

    return backtrack(0)
  ```
