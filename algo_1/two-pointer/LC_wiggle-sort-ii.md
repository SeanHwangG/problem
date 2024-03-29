# [LC_wiggle-sort-ii](https://leetcode.com/problems/wiggle-sort-ii)

* en

  ```en
  Given int array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]...
  Assume input array always has valid answer
  ```

* tc

  ```tc
  Input: nums = [1,5,1,1,6,4]
  Output: [1,6,1,5,1,4]
  ```

## Solution

* cpp

  ```cpp
  void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    auto midptr = nums.begin() + n / 2;
    nth_element(nums.begin(), midptr, nums.end());
    int mid = *midptr;
    #define A(i) nums[(1+2*(i)) % (n|1)]

    // 3-way-partition-to-wiggly in O(n) time with O(1) space.
    int i = 0, j = 0, k = n - 1;
    while (j <= k) {
      if (A(j) > mid)
        swap(A(i++), A(j++));
      else if (A(j) < mid)
        swap(A(j), A(k--));
      else
        j++;
    }
  }
  ```
