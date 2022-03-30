# [LC_serialize-and-deserialize-n-ary-tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree)

Design an algorithm to serialize and deserialize an N-ary tree

```txt
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

## Solution

```py
class Codec:
  def serialize(self, root):
    if not root:
        return []

    if not root.children:
        return root.val

    return [root.val, [self.serialize(c) for c in root.children]]

  def deserialize(self, data):
    if data == []:
        return None

    if isinstance(data, int):
      return Node(data, [])

    return Node(val = data[0], children = [self.deserialize(c) for c in data[1]])
```
