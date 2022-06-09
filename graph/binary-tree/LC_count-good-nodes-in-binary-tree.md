# [LC_count-good-nodes-in-binary-tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree)

* en

  ```en
  Count number of good nodes in a binary tree
  ```

* tc

  ```tc
  Input: root = [3,1,4,3,null,1,5]
  Output: 4
  ```

## Solution

* cpp
  * Time; O(N)
  * Space; O(height)

  ```cpp
  int goodNodes(TreeNode* r, int ma = -10000) {
    return r? goodNodes(r->left, max(ma, r->val)) + goodNodes(r->right, max(ma, r->val)) + (r->val >= ma): 0;
  }
  ```

* py
  * Time: O(N)
  * Space: O(height)

  ```py
  def goodNodes(self, r, ma=-10000):
    return self.goodNodes(r.left, max(ma, r.val)) + self.goodNodes(r.right, max(ma, r.val)) + (r.val >= ma) if r
      else 0
  ```
