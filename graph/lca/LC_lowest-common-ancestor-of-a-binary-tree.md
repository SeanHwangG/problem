# [LC_lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)

```en
Find loest common ancestor of p and q
```

```txt
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

## Solution

* Time / space; O(n) / O(n)

* py

  ```py
  def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
    return root if left and right else left or right
  ```
