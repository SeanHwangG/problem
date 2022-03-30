# [LC_same-tree](https://leetcode.com/problems/same-tree)

Check if tree are same

```txt
Input: p = [1,2], q = [1,null,2]
Output: false
```

## Solution

```py
def isSameTree(self, p, q):
  if p and q:
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  return p is q
```
