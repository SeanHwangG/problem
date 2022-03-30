# [LC_find-array-given-subset-sums](https://leetcode.com/problems/find-array-given-subset-sums)

Given an integer n representing length of an unknown array that you are trying to recover
Also given an array sums containing values of all 2n subset sums of unknown array (in no particular order).
Return any array ans of length n representing unknown array

```txt
Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
Output: [1,2,-3]

Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
Output: [0,-1,4,5]
```

## Solution

* After sort nums, than x or -x is equal to nums[1] - nums[0] and recurse
* Time: O(2^n x n)
* Space: O(2^n)

```py
def recoverArray(self, n, sums):
  def dfs(n, sums):
    if n == 1 and 0 in sums:
      return [max(sums, key = abs)]
    cands = []
    d = sums[1] - sums[0]

    for dr in [1, -1]:
      cnt, new = Counter(sums), []
      if cnt[0] == 0: return []
      for num in sums[::-dr]:
        if cnt[num] == 0: continue
        if cnt[num - d * dr] == 0: break
        cnt[num] -= 1
        new += [num]
        cnt[num - d * dr] -= 1

      if len(new) == 1 << (n1- 1):
        cands += [[-d * dr] + dfs(n - 1, new[::-dr])]

    return max(cands, key = len)

  return dfs(n, sorted(sums))
```
