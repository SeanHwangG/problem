# [LC_insert-delete-getrandom-o1-duplicates-allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed)

* en

  ```en
  Implement the RandomizedCollection class:
    RandomizedCollection(): Initializes RandomizedCollection object
    bool insert(int val): Insert item val into multiset if not present. Returns if item not present
    bool remove(int val) Remove 1 item val from multiset if present. Returns if item is present
    int getRandom() Returns a random element from current multiset of elements
      it's guaranteed that at least 1 element exists when this method is called
  Probability of each element being returned is linearly related to number of same values multiset contains
  ```

* tc

  ```tc
  Input:
  ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
  [[], [1], [1], [2], [], [1], []]

  Output:
  [null, true, false, true, 2, true, 1]
  ```

## Solution

* java

  ```java
  public class RandomizedCollection {
    ArrayList<Integer> nums;
    HashMap<Integer, Set<Integer>> locs;
    java.util.Random rand = new java.util.Random();

    public RandomizedCollection() {
      nums = new ArrayList<Integer>();
      locs = new HashMap<Integer, Set<Integer>>();
    }

    /* Inserts value to the collection. Returns true if the collection did not already contain the specified element */
    public boolean insert(int val) {
      boolean contain = locs.containsKey(val);
      if (!contain) locs.put(val, new LinkedHashSet<Integer>());
      locs.get(val).add(nums.size());
      nums.add(val);
      return ! contain ;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
      boolean contain = locs.containsKey(val);
      if (!contain) return false;
      int loc = locs.get(val).iterator().next();
      locs.get(val).remove(loc);
      if (loc < nums.size() - 1) {
        int lastone = nums.get(nums.size() - 1);
        nums.set(loc , lastone);
        locs.get(lastone).remove( nums.size()-1);
        locs.get(lastone).add(loc);
      }
      nums.remove(nums.size() - 1);

      if (locs.get(val).isEmpty()) locs.remove(val);
      return true;
    }

    /** Get a random element from the collection. */
    public int getRandom() {
      return nums.get(rand.nextInt(nums.size()));
    }
  }
  ```

* py

  ```py
  import random

  class RandomizedCollection(object):
    def __init__(self):
      self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
      self.vals.append(val)
      self.idxs[val].add(len(self.vals) - 1)
      return len(self.idxs[val]) == 1

    def remove(self, val):
      if self.idxs[val]:
        out, ins = self.idxs[val].pop(), self.vals[-1]
        self.vals[out] = ins
        if self.idxs[ins]:
          self.idxs[ins].add(out)
          self.idxs[ins].discard(len(self.vals) - 1)
        self.vals.pop()
        return True
      return False

    def getRandom(self):
        return random.choice(self.vals)
  ```
