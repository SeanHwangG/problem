# [LC_design-hashmap](https://leetcode.com/problems/design-hashmap)

MyHashMap() initializes the object with an empty map
void put(int key, int value) inserts a (key, value) pair into the HashMap
  If the key already exists in the map, update the corresponding value
int get(int key) returns the value to which the specified key is mapped
  -1 if this map contains no mapping for the key
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key

```txt
Input:
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output: [null, null, null, 1, -1, null, 1, null, -1]
```

## Solution

```cpp
struct Node {
public:
  int key, val;
  Node* next;
  Node(int k, int v, Node* n): key (k), val (v), next (n) {}
};
class MyHashMap {
public:
  const static int size = 19997;
  const static int mult = 12582917;
  Node* data[size];
  int hash(int key) {
    return (int)((long)key * mult % size);
  }
  void put(int key, int val) {
    remove(key);
    int h = hash(key);
    Node* node = new Node(key, val, data[h]);
    data[h] = node;
  }
  int get(int key) {
    int h = hash(key);
    Node* node = data[h];
    for (; node != NULL; node = node->next)
      if (node->key == key) return node->val;
    return -1;
  }
  void remove(int key) {
    int h = hash(key);
    Node* node = data[h];
    if (node == NULL) return;
    if (node->key == key) data[h] = node->next;
    else
      for (; node->next != NULL; node = node->next)
        if (node->next->key == key) {
          node->next = node->next->next;
          return;
        }
  }
};
```

```java
class MyHashMap {
  final ListNode[] nodes = new ListNode[10000];

  public void put(int key, int value) {
    int i = idx(key);
    if (nodes[i] == null)
      nodes[i] = new ListNode(-1, -1);
    ListNode prev = find(nodes[i], key);
    if (prev.next == null)
      prev.next = new ListNode(key, value);
    else prev.next.val = value;
  }

  public int get(int key) {
    int i = idx(key);
    if (nodes[i] == null)
      return -1;
    ListNode node = find(nodes[i], key);
    return node.next == null ? -1 : node.next.val;
  }

  public void remove(int key) {
    int i = idx(key);
    if (nodes[i] == null) return;
    ListNode prev = find(nodes[i], key);
    if (prev.next == null) return;
    prev.next = prev.next.next;
  }

  int idx(int key) { return Integer.hashCode(key) % nodes.length;}

  ListNode find(ListNode bucket, int key) {
    ListNode node = bucket, prev = null;
    while (node != null && node.key != key) {
      prev = node;
      node = node.next;
    }
    return prev;
  }

  class ListNode {
    int key, val;
    ListNode next;

    ListNode(int key, int val) {
      this.key = key;
      this.val = val;
    }
  }
}
```

```js
class ListNode {
  constructor(key, val, next) {
    this.key = key
    this.val = val
    this.next = next
  }
}
class MyHashMap {
  constructor() {
    this.size = 19997
    this.mult = 12582917
    this.data = new Array(this.size)
  }
  hash(key) { return key * this.mult % this.size }
  put(key, val) {
    this.remove(key)
    let h = this.hash(key)
    let node = new ListNode(key, val, this.data[h])
    this.data[h] = node
  }
  get(key) {
    let h = this.hash(key), node = this.data[h]
    for (; node; node = node.next)
      if (node.key === key) return node.val
    return -1
  }
  remove(key) {
    let h = this.hash(key), node = this.data[h]
    if (!node) return
    if (node.key === key) this.data[h] = node.next
    else for (; node.next; node = node.next)
      if (node.next.key === key) {
        node.next = node.next.next
        return
      }
  }
};
```

```py
class ListNode:
  def __init__(self, key = None, val = None):
    self.pair = (key, val)
    self.next = None

class MyHashMap:
  def __init__(self):
    self.m = 1000
    self.h = [ListNode() for _ in range(self.m)]

  def put(self, key, value):
    idx = key % self.m
    cur = self.h[idx]
    while True:
      if cur.pair[0] == key:
        cur.pair = (key, value)
        return
      if cur.next == None:
        break
      cur = cur.next
    cur.next = ListNode(key, value)

  def get(self, key):
    idx = key % self.m
    cur = self.h[idx]
    while cur:
      if cur.pair[0] == key:
        return cur.pair[1]
      cur = cur.next
    return -1

  def remove(self, key):
    idx = key % self.m
    cur = prev = self.h[idx]
    cur = cur.next

    while cur:
      if cur.pair[0] == key:
        prev.next = cur.next
        break
      cur, prev = cur.next, prev.next
```
