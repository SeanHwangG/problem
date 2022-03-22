{% tabs %}{% tab title='LC_559.cpp' %}

```cpp
int maxDepth(Node* root) {
  if (root == nullptr) return 0;
  int depth = 0;
  for (auto child : root->children) depth = max(depth, maxDepth(child));
  return 1 + depth;
}
```

{% endtab %}{% tab title='LC_559.py' %}

```py
def maxDepth(self, root):
  if not root: return 0
  return 1 + max(map(self.maxDepth, root.children or [None]))
```

{% endtab %}{% endtabs %}