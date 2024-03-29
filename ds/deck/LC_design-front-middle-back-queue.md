# [LC_design-front-middle-back-queue](https://leetcode.com/problems/design-front-middle-back-queue)

* en

  ```en
  Design a queue that supports push and pop operations in the front, middle, and back.
  Implement the FrontMiddleBack class:
    FrontMiddleBack() Initializes the queue
    void pushFront(int val) Adds val to the front of the queue
    void pushMiddle(int val) Adds val to the middle of the queue (performed on the frontmost middle position choice)
    void pushBack(int val) Adds val to the back of the queue
    int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1
    int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1
    int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1
  ```

* tc

  ```tc
  Input:
  ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle",
    "popBack", "popFront"]
  [[], [1], [2], [3], [4], [], [], [], [], []]

  Output:
  [null, null, null, null, null, 1, 3, 4, 2, -1]
  ```

## Solution

* py

  ```py
  class FrontMiddleBackQueue(object):
    def __init__(self):
      self.A, self.B = collections.deque(), collections.deque()

    def pushFront(self, val):
      self.A.appendleft(val)
      self.balance()

    def pushMiddle(self, val):
      if len(self.A) > len(self.B):
        self.B.appendleft(self.A.pop())
      self.A.append(val)

    def pushBack(self, val):
      self.B.append(val)
      self.balance()

    def popFront(self):
      val = self.A.popleft() if self.A else -1
      self.balance()
      return val

    def popMiddle(self):
      val = (self.A or [-1]).pop()
      self.balance()
      return val

    def popBack(self):
      val = (self.B or self.A or [-1]).pop()
      self.balance()
      return val

    # keep A.size() >= B.size()
    def balance(self):
      if len(self.A) > len(self.B) + 1:
        self.B.appendleft(self.A.pop())
      if len(self.A) < len(self.B):
        self.A.append(self.B.popleft())
  ```
