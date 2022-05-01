# [LC_delete-duplicate-folders-in-system](https://leetcode.com/problems/delete-duplicate-folders-in-system)

There are duplicate folders in a file system
given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in file system
Two folders (not necessarily on the same level) are identical
if they contain the same non-empty set of identical subfolders and underlying subfolder structure
folders do not need to be at the root level to be identical
If two or more folders are identical, then mark the folders as well as all their subfolders.
Return 2D array ans containing paths of remaining folders after deleting all marked folders (in any order)

```txt
Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
Output: [["d"],["d","a"]]

Input: paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
Output: [["c"],["c","b"],["a"],["a","b"]]
```

## Solution

* py

  ```py
  class Node:
    def __init__(self):
      self.child = defaultdict(Node)
      self.dl = False

  class Solution:
    def deleteDuplicateFolder(self, paths):
      def dfs1(node):
        key = f"({''.join(c + dfs1(node.child[c]) for c in node.child)})"
        if key != "()":
          pattern[key].append(node)
        return key

      def dfs2(node, path):
        for c in node.child:
          if not node.child[c].dl:
            dfs2(node.child[c], path + [c])
        if path:
          ans.append(path[:])

      pattern, root, ans = defaultdict(list), Node(), []

      for path in paths:
        node = root
        for c in path:
          node = node.child[c]
      dfs1(root)

      for nodes in pattern.values():
        for i in nodes:
          i.dl = len(nodes) > 1
      dfs2(root, [])
      return ans
  ```
