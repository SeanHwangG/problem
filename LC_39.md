{% tabs %}{% tab title='LC_39.md' %}

* Given an array of distinct integers candidates and a target integer target
* return a list of all unique combinations of candidates where the chosen numbers sum to target
* You may return the combinations in any order

```txt
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

{% endtab %}{% tab title='LC_39.go' %}

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

{% endtab %}{% tab title='LC_39.py' %}

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

{% endtab %}{% endtabs %}
