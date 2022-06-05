# [LC_nested-list-weight-sum-ii](https://leetcode.com/problems/nested-list-weight-sum-ii)

```en
Given nested list of ints nestedList, Each element is int or list whose elements may also be ints or other lists
Depth is number of lists that it is inside of, weight of an int is maxDepth - (depth of the int) + 1
Return sum of each int in nestedList multiplied by its weight.
```

```txt
Input: nestedList = [[1,1],2,[1,1]]
Output: 8  # 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

Input: nestedList = [1,[4,[6]]]
Output: 17  # 1*3 + 4*2 + 6*1 = 17
```

## Solution

* py

  ```py
  def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    unweighted = 0
    weighted = 0
    while nestedList:
      nextLevel = []
      for item in nestedList:
        if item.isInteger():
          unweighted += item.getInteger()
        else:
          nextLevel.extend(item.getList())
      weighted += unweighted
      nestedList = nextLevel
    return weighted
  ```
