{% tabs %}{% tab title='LC_684.cpp' %}

```cpp
vector<int> findRedundantConnection(vector<vector<int>>& edges) {
  vector<int> parent(edges.size()+1, 0);
  for (auto &e: edges) {
    int v1 = e[0], v2 = e[1];
    while (parent[v1]) v1 = parent[v1];
    while (parent[v2]) v2 = parent[v2];
    if (v1 == v2) return e;
    parent[v1] = v2;
  }
}
```

{% endtab %}{% tab title='LC_684.py' %}

* Time; O(n^2) because of string replace / Space : O(n)

```py
def findRedundantConnection(self, edges):
  tree = ''.join(map(chr, range(1001)))
  for u, v in edges:
    if tree[u] == tree[v]:
      return [u, v]
    tree = tree.replace(tree[u], tree[v])
```

{% endtab %}{% endtabs %}
