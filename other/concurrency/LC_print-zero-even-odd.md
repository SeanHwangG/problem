# [LC_print-zero-even-odd](https://leetcode.com/problems/print-zero-even-odd)

Thread A will call zero() which should only output 0's
Thread B will call even() which should only ouput even numbers
Thread C will call odd() which should only output odd numbers

```txt
Input: n = 5
Output: "0102030405"
```

## Solution

* lock

* cpp

```cpp
class ZeroEvenOdd {
private:
  int n;
  mutex em, om, zm;

public:
  ZeroEvenOdd(int n) {
    em.lock();
    om.lock();
    this->n = n;
  }

  // printNumber(x) outputs "x", where x is an integer.
  void zero(function<void(int)> printNumber) {
    for (int i = 0; i < n; i++) {
      zm.lock();
      printNumber(0);
      if (i % 2 == 0) om.unlock();
      else            em.unlock();
    }
  }

  void even(function<void(int)> printNumber) {
    for (int i = 2; i <= n; i+=2){
      em.lock();
      printNumber(i);
      zm.unlock();
    }
  }

  void odd(function<void(int)> printNumber) {
    for (int i = 1; i <= n; i+=2){
      om.lock();
      printNumber(i);
      zm.unlock();
    }
  }
};
```

* Semaphore

* java

```java
import java.util.concurrent.*;
class ZeroEvenOdd {
  private int n;
  private Semaphore zeroSem, oddSem, evenSem;

  public ZeroEvenOdd(int n) {
    this.n = n;
    zeroSem = new Semaphore(1);
    oddSem = new Semaphore(0);
    evenSem = new Semaphore(0);
  }

  // printNumber.accept(x) outputs "x", where x is an integer.
  public void zero(IntConsumer printNumber) throws InterruptedException {
    for (int i = 0; i < n; ++i) {
      zeroSem.acquire();
      printNumber.accept(0);
      (i % 2 == 0 ? oddSem : evenSem).release(); // Alternately release odd() and even().
    }
  }

  public void even(IntConsumer printNumber) throws InterruptedException {
    for (int i = 2; i <= n; i += 2) {
      evenSem.acquire();
      printNumber.accept(i);
      zeroSem.release();
    }
  }

  public void odd(IntConsumer printNumber) throws InterruptedException {
    for (int i = 1; i <= n; i += 2) {
      oddSem.acquire();
      printNumber.accept(i);
      zeroSem.release();
    }
  }
}
```

* Condition

* py

```py
from threading import Condition

class ZeroEvenOdd:
  def __init__(self, n):
    self.n = n
    self.sem = 0
    self.c = Condition()

  def zero(self, printNumber: 'Callable[[int], None]') -> None:
    for i in range(self.n):
      with self.c:
        while self.sem:
          self.c.wait()
        printNumber(0)
        self.sem = 2 if i % 2 else 1
        self.c.notify_all()

  def even(self, printNumber: 'Callable[[int], None]') -> None:
    for i in range(2, self.n + 1, 2):
      with self.c:
        while self.sem - 2:
          self.c.wait()
        printNumber(i)
        self.sem = 0
        self.c.notify_all()

  def odd(self, printNumber: 'Callable[[int], None]') -> None:
    for i in range(1, self.n + 1, 2):
      with self.c:
        while self.sem - 1:
          self.c.wait()
        printNumber(i)
        self.sem = 0
        self.c.notify_all()
```
