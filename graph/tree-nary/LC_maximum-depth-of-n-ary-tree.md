# [LC_maximum-depth-of-n-ary-tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree)

* en

  ```en
  Print depth of tree
  ```

* tc

  ```tc
  Input: root = [1,null,3,2,4,null,5,6]
  Output: 3
  ```

## Solution

* cpp

  ```cpp
  int maxDepth(Node* root) {
    if (root == nullptr) return 0;
    int depth = 0;
    for (auto child : root->children) depth = max(depth, maxDepth(child));
    return 1 + depth;
  }
  ```

* py

  ```py
  def maxDepth(self, root):
    if not root: return 0
    return 1 + max(map(self.maxDepth, root.children or [None]))
  ```
