# [LC_validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree)

```en
Check if tree is valid BST
```

```txt
Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    bool isValidBST(TreeNode* root, long min = LONG_MIN, long max = LONG_MAX) {
      if (root == NULL) return true;
      if (root->val <= min || root->val >= max) return false;
      return isValidBST(root->left, min, root->val) && isValidBST(root->right, root->val, max);
    }
  };
  ```

* py

  ```py
  def isValidBST(self, root: TreeNode, left = float('-inf'), right = float('inf')) -> bool:
    return not root or left < root.val < right and \
        self.isValidBST(root.left, left, root.val) and \
        self.isValidBST(root.right, root.val, right)
  ```
