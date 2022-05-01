# [LC_house-robber-iii](https://leetcode.com/problems/house-robber-iii)

Automatically contact police if two directly-linked houses were broken into on same night
Determine maximum amount of money thief can rob tonight without alerting police

```txt
Input: root = [3,2,3,null,3,null,1]
Output: 7
```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    int rob(TreeNode* root) {
      auto [best_with_root, best_without_root] = rob_helper(root);
      return max(best_with_root, best_without_root);
    }

    std::pair<int, int> rob_helper(TreeNode* root) {
      if (!root)
        return {0, 0};
      auto [l_with_node, l_wo_node] = rob_helper(root->left);
      auto [r_with_node, r_wo_node] = rob_helper(root->right);

      return {root->val + l_wo_node + r_wo_node, max(l_with_node, l_wo_node) + max(r_with_node, r_wo_node)};
    }
  };
  ```

* py

  ```py
  def rob(self, root: TreeNode):
    def with_without_rob(root):
      if root :
        wi_l, wo_l = with_without_rob(root.left)
        wi_r, wo_r = with_without_rob(root.right)
        return (root.val + wo_l + wo_r, max(wi_l, wo_l) + max(wi_r, wo_r))
      return (0, 0)

    return max(with_without_rob(root))
  ```
