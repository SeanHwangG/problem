# [LC_all-oone-data-structure](https://leetcode.com/problems/all-oone-data-structure)

* en

  ```en
  Implement AllOne class:
  AllOne() Initializes object of data structure.
  inc(String key) Increments count of string key by 1. If key not exist in data structure, insert with count 1
  dec(String key) Decrements count of string key by 1. If count of key is 0 after decrement, remove it
    It is guaranteed that key exists in data structure before decrement
  getMaxKey() Returns one of keys with max count. If no element exists, return an empty string ""
  getMinKey() Returns one of keys with min count. If no element exists, return an empty string ""
  ```

* tc

  ```tc
  Input:
  ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
  [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
  Output:
  [null, null, null, "hello", "hello", null, "hello", "leet"]
  ```

## Solution

* cpp

  ```cpp
  class AllOne {
  public:
    void inc(string key) {
      if (!bucketOfKey.count(key)) // If the key doesn't exist, insert it with value 0.
        bucketOfKey[key] = buckets.insert(buckets.begin(), {0, {key}});

      // Insert the key in next bucket and update the lookup.
      auto next = bucketOfKey[key], bucket = next++;
      if (next == buckets.end() || next->value > bucket->value + 1)
        next = buckets.insert(next, {bucket->value + 1, {}});
      next->keys.insert(key);
      bucketOfKey[key] = next;

      bucket->keys.erase(key); // Remove the key from its old bucket.
      if (bucket->keys.empty())
        buckets.erase(bucket);
    }

    void dec(string key) {
      if (!bucketOfKey.count(key)) // If the key doesn't exist, just leave.
        return;

      // Maybe insert the key in previous bucket and update the lookup.
      auto prev = bucketOfKey[key], bucket = prev--;
      bucketOfKey.erase(key);
      if (bucket->value > 1) {
        if (bucket == buckets.begin() || prev->value < bucket->value - 1)
          prev = buckets.insert(bucket, {bucket->value - 1, {}});
        prev->keys.insert(key);
        bucketOfKey[key] = prev;
      }

      // Remove the key from its old bucket.
      bucket->keys.erase(key);
      if (bucket->keys.empty())
        buckets.erase(bucket);
    }

    string getMaxKey() {
      return buckets.empty() ? "" : *(buckets.rbegin()->keys.begin());
    }

    string getMinKey() {
      return buckets.empty() ? "" : *(buckets.begin()->keys.begin());
    }

  private:
    struct Bucket { int value; unordered_set<string> keys; };
    list<Bucket> buckets;
    unordered_map<string, list<Bucket>::iterator> bucketOfKey;
  };
  ```

* py

  ```py
  class Block(object):
    def __init__(self, val=0):
      self.val = val
      self.keys = set()
      self.before, self.after = None, None

    def remove(self):
      self.before.after, self.after.before = self.after, self.before
      self.before, self.after = None, None

    def insert_after(self, new_block):
      old_after = self.after
      self.after = new_block
      new_block.before = self
      new_block.after = old_after
      old_after.before = new_block


  class AllOne(object):
    def __init__(self):
      self.begin, self.end = Block(), Block()  # sentinel
      self.begin.after, self.end.before = self.end, self.begin
      self.mapping = {}  # key to block

    def inc(self, key):
      if not key in self.mapping:  # find current block and remove key
        current_block = self.begin
      else:
        current_block = self.mapping[key]
        current_block.keys.remove(key)

      if current_block.val + 1 != current_block.after.val:  # insert new block
        new_block = Block(current_block.val + 1)
        current_block.insert_after(new_block)
      else:
        new_block = current_block.after

      new_block.keys.add(key)  # update new_block
      self.mapping[key] = new_block  # ... and mapping of key to new_block

      if not current_block.keys and current_block.val != 0:  # delete current block if not seninel
        current_block.remove()

    def dec(self, key):
      if not key in self.mapping:
        return

      current_block = self.mapping[key]
      del self.mapping[key]  # could use self.mapping.pop(key)
      current_block.keys.remove(key)

      if current_block.val != 1:
        if current_block.val - 1 != current_block.before.val:  # insert new block
          new_block = Block(current_block.val - 1)
          current_block.before.insert_after(new_block)
        else:
          new_block = current_block.before
        new_block.keys.add(key)
        self.mapping[key] = new_block

      if not current_block.keys:  # delete current block
        current_block.remove()

    def getMaxKey(self):
      if self.end.before.val == 0:
        return ""
      key = self.end.before.keys.pop()  # pop and add back to get arbitrary (but not random) element
      self.end.before.keys.add(key)
      return key

    def getMinKey(self):
      if self.begin.after.val == 0:
        return ""
      key = self.begin.after.keys.pop()
      self.begin.after.keys.add(key)
      return key
  ```
