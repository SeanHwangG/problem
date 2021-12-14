{% tabs %}{% tab title='LC_428.py' %}

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

{% endtab %}{% endtabs %}
