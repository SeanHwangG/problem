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

```py
def isValidBST(self, root: TreeNode, left = float('-inf'), right = float('inf')) -> bool:
  return not root or left < root.val < right and \
      self.isValidBST(root.left, left, root.val) and \
      self.isValidBST(root.right, root.val, right)
```
