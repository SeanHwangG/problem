# [LC_permutations](https://leetcode.com/problems/permutations)

* en

  ```en
  Given array nums of distinct integers, return all the possible permutations. You can return the answer in any order
  ```

* tc

  ```tc
  Input: nums = [1,2,3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
  Example 2:

  Input: nums = [0,1]
  Output: [[0,1],[1,0]]
  ```

## Solution

* go

  ```go
  func permute(nums []int) [][]int {
    if len(nums) == 0
      return nil
    ans := make([][]int, 0)
    backtrack(nums, nil, &ans)

    return ans
  }

  func backtrack(nums []int, prev []int, ans *[][]int) {
    if len(nums) == 0 {
      *ans = append(*ans, append([]int{}, prev...))
      return
    }

    for i := 0; i < len(nums); i++ {
      backtrack(append(append([]int{}, nums[0:i]...), nums[i+1:]...),
        append(prev, nums[i]), ans)
    }
  }
  ```
