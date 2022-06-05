# [LC_combination-sum](https://leetcode.com/problems/combination-sum)

```en
Given an array of distinct integers candidates and a target integer target
Return list of all unique combinations of candidates where chosen numbers sum to target in any order
```

```txt
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

## Solution

* go

  ```go
  func combinationSum(candidates []int, target int) [][]int {
    result := make([][]int, 0)
    backtracking([]int{}, candidates, 0, target, &result)
    return result
  }

  func backtracking(subset, candidates []int, sum, target int, result *[][]int) {
    if sum == target {
      *result = append(*result, subset)
      return
    } else if sum > target {
      return
    }
    for i := range candidates {
      subsetCopy := make([]int, 0)
      subsetCopy = append(subsetCopy, subset...)
      backtracking(append(subsetCopy, candidates[i]), candidates[i:], sum + candidates[i], target, result)
    }
  }
  ```

* py

  ```py
  def combinationSum(self, candidates, target):
    res = []
    candidates.sort()

    def dfs(target, index, path):
      if target < 0:
        return
      if target == 0:
        res.append(path)
        return
      for i in range(index, len(candidates)):
        dfs(target-candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])
    return res
  ```
