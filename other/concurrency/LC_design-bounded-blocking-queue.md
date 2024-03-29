# [LC_design-bounded-blocking-queue](https://leetcode.com/problems/design-bounded-blocking-queue)

* en

  ```en
  BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity
  void enqueue(int element) Adds an element to front of queue. If full, calling thread is blocked until no longer full
  int dequeue() Return element at rear of queue and remove it. If empty, calling thread is blocked until no longer empty
  int size() Returns the number of elements currently in the queue
  ```

* tc

  ```tc
  Input:
  1
  1
  ["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
  [[2],[1],[],[],[0],[2],[3],[4],[]]

  Output:
  [1,0,2,2]
  ```

## Solution

* cpp
  * Condition variable
  * Time; O(n)
  * Space; O(1)

  ```cpp
  class BoundedBlockingQueue {
  public:
    BoundedBlockingQueue(int capacity) : cap_(capacity) {}
    void enqueue(int element) {
      {
        unique_lock<mutex> l(m_);
        cv_.wait(l, [this]() { return q_.size() != cap_; }) ;
        q_.emplace(element);
      }
      cv_.notify_all();
    }

    int dequeue() {
      int element;
      {
        unique_lock<mutex> l(m_);
        cv_.wait(l, [this]() { return !q_.empty(); }) ;
        element = q_.front(); q_.pop();
      }
      cv_.notify_all();
      return element;
    }

    int size() {
      unique_lock<mutex> l(m_);
      return q_.size();
    }

  private:
    mutex m_;
    condition_variable cv_;
    queue<int> q_;
    int cap_;
  };
  ```

* py

  ```py
  # Semaphore
  import threading

  class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
      self.capacity = capacity

      self.pushing = threading.Semaphore(capacity)
      self.pulling = threading.Semaphore(0)
      self.editing = threading.Lock()

      self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
    self.pushing.acquire()
    self.editing.acquire()

    self.queue.append(element)

    self.editing.release()
    self.pulling.release()

    def dequeue(self) -> int:
      self.pulling.acquire()
      self.editing.acquire()

      res = self.queue.popleft()

      self.editing.release()
      self.pushing.release()
      return res

    def size(self) -> int:
      return len(self.queue)

  # Condition variable: Time; O(n), Space; O(1)
  import threading

  class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
      self.cv = threading.Condition()
      self.q = collections.deque()
      self.capa = capacity
      self.count = 0

    def enqueue(self, element: int) -> None:
      with self.cv:
        while self.count == self.capa:
          self.cv.wait()
        self.q.append(element)
        self.count += 1
        self.cv.notify()

    def dequeue(self) -> int:
      val = 0
      with self.cv:
        while self.count == 0:
          self.cv.wait()
        val = self.q.popleft()
        self.count -= 1
        self.cv.notify()
      return val

    def size(self) -> int:
      with self.cv:
        return len(self.q)
  ```
