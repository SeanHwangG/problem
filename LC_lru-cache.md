{% tabs %}{% tab title='LC_146.py' %}

```py
class LRUCache:
  def __init__(self, Capacity):
    self.size = Capacity
    self.cache = OrderedDict()

  def get(self, key):
    if key not in self.cache: return -1
    val = self.cache[key]
    self.cache.move_to_end(key)
    return val

  def put(self, key, val):
    self.cache.pop(key, None)
    self.cache[key] = val
    if len(self.cache) > self.size:
      self.cache.popitem(last=False)
```

{% endtab %}{% endtabs %}
