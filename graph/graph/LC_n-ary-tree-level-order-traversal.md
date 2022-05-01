# [LC_n-ary-tree-level-order-traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal)

Given an n-ary tree, return the level order traversal of its nodes' values

```txt
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

## Solution

* py

  ```py
  def levelOrder(self, root):
    q, ret = [root], []
    while any(q):
      ret.append([node.val for node in q])
      q = [child for node in q for child in node.children if child]
    return ret
  ```
