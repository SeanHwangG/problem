# [LC_dinner-plate-stacks](https://leetcode.com/problems/dinner-plate-stacks)

Implement the DinnerPlates class:
DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
int pop() Return value at top of rightmost non-empty stack and removes it from that stack, -1 if all stacks are empty
int popAtStack(int index) Return value at top of stack with given index, and removes it from that stack or -1 if empty

```txt
Input
["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop",
 "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
Output
[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
```

## Solution

* cpp
  * Time: push=O(logN), pop=amortized O(1), popAtStack=O(logN)

  ```cpp
  int c;
  map<int, vector<int>> m;
  set<int> available;

  DinnerPlates(int capacity) {
    c = capacity;
  }

  void push(int val) {
    if (available.empty())
      available.insert(m.size());
    m[*available.begin()].push_back(val);
    if (m[*available.begin()].size() == c)
      available.erase(available.begin());
  }

  int pop() {
    while (m.size() && m.rbegin()->second.empty())
      m.erase(m.rbegin()->first);

    if (m.empty()) return -1;
    return popAtStack(m.rbegin()->first);
  }

  int popAtStack(int index) {
    if (m[index].empty())
      return -1;
    int val = m[index].back();
    m[index].pop_back();
    available.insert(index);
    if (m[index].empty())
      m.erase(index);
    return val;
  }
  ```

* py

  ```py
  class DinnerPlates:
    def __init__(self, capacity):
      self.c, self.q, self.stacks = capacity, [], []  # q=available stack, stacks=list of stacks

    def push(self, val):
      while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
        heapq.heappop(self.q)
      if not self.q:  # Add new stack as there are no available stakcs
        heapq.heappush(self.q, len(self.stacks))
      if self.q[0] == len(self.stacks):
        self.stacks.append([])
      self.stacks[self.q[0]].append(val)  # append the value to the leftmost available stack

    def pop(self):
      while self.stacks and not self.stacks[-1]:
        self.stacks.pop()
      return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
      if 0 <= index < len(self.stacks) and self.stacks[index]:
        heapq.heappush(self.q, index)
        return self.stacks[index].pop()
      return -1
  ```
