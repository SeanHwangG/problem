# [LC_fizz-buzz-multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded)

```en
Print fizz buzz given 4 threads
  a thread printing fizz
  a thread printing buzz
  a thread printing fizzbuzz
  a thread incrementing a number
```

```txt
Input: n = 15
Output: [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
```

## Solution

* cpp

  ```cpp
  class FizzBuzz {
    private:
      int n;
      atomic<int> current;
      mutex mx;
      condition_variable cv;
    public:
      FizzBuzz(int n) {
        this->n = n;
        current = 1;
      }

      void fizz(function<void()> printFizz) {
        do_work([&](int i){printFizz();}, [&]{ return (current % 3 == 0 && current % 5 != 0);});
      }

      void buzz(function<void()> printBuzz) {
        do_work([&](int i){printBuzz();}, [&]{ return (current % 5 == 0 && current % 3 != 0);});
      }

      void fizzbuzz(function<void()> printFizzBuzz) {
        do_work([&](int i){printFizzBuzz();}, [&]{ return (current % 5 == 0 && current % 3 == 0);});
      }

      void number(function<void(int)> printNumber)  {
        do_work(printNumber, [&]{ return (current % 5 != 0 && current % 3 != 0);});
      }
    protected:
      void do_work(function<void(int)> printFunc, function<bool()> evalFunc) {
        while(current <= n) {
          unique_lock<mutex> ul(mx);
          cv.wait(ul, [&]{ return (evalFunc() || current > n);});
          if(current > n) break;
          printFunc(current);
          ++current;
          cv.notify_all();
        }
      }
  };
  ```

* py

  ```py
  from threading import Semaphore
  class FizzBuzz(object):
    def __init__(self, n):
      self.n = n
      self.sem0 = Semaphore(1)
      self.sem3 = Semaphore(0)
      self.sem5 = Semaphore(0)
      self.sem15 = Semaphore(0)
    def fizz(self, printFizz):
      for i in range(3, self.n + 1, 3):
        if i % 15:
          self.sem3.acquire()
          printFizz()
          self._release(i+1)

    def buzz(self, printBuzz):
      for i in range(5, self.n + 1, 5):
        if i % 15:
          self.sem5.acquire()
          printBuzz()
          self._release(i+1)

    def fizzbuzz(self, printFizzBuzz):
      for i in range(15, self.n + 1, 15):
        self.sem15.acquire()
        printFizzBuzz()
        self._release(i+1)

    def number(self, printNumber):
      for i in range(1, self.n + 1):
        if i % 3 and i % 5:
          self.sem0.acquire()
          printNumber(i)
          self._release(i+1)

    def _release(self, i):
      if i % 3 and i % 5:
        self.sem0.release()
      elif i % 5:
        self.sem3.release()
      elif i % 3:
        self.sem5.release()
      else:
        self.sem15.release()
  ```
