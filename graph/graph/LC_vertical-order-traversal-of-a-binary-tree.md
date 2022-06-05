# [LC_vertical-order-traversal-of-a-binary-tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree)

```en
Given the root of a binary tree, calculate the vertical order traversal of the binary tree
```

```txt
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
```

## Solution

* py

  ```py
  def verticalTraversal(self, root):
    g = collections.defaultdict(list)
    queue = [(root,0)]
    while queue:
      new = []
      d = collections.defaultdict(list)
      for node, s in queue:
        d[s].append(node.val)
        if node.left:  new += (node.left, s-1),
        if node.right: new += (node.right,s+1),
      for i in d: g[i].extend(sorted(d[i]))
      queue = new
    return [g[i] for i in sorted(g)]
  ```
