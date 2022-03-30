* Time; O(N)
* Space; O(height)

```cpp
int goodNodes(TreeNode* r, int ma = -10000) {
  return r? goodNodes(r->left, max(ma, r->val)) + goodNodes(r->right, max(ma, r->val)) + (r->val >= ma): 0;
}
```

* Time: O(N)
* Space: O(height)

```py
def goodNodes(self, r, ma=-10000):
  return self.goodNodes(r.left, max(ma, r.val)) + self.goodNodes(r.right, max(ma, r.val)) + (r.val >= ma) if r
    else 0
```