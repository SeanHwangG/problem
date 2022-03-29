* Promise

```cpp
class Foo {
private:
  std::promise<void> p1;
  std::promise<void> p2;

public:
  void first(function<void()> printFirst) {
    printFirst();
    p1.set_value();
  }

  void second(function<void()> printSecond) {
    p1.get_future().wait();
    printSecond();
    p2.set_value();
  }

  void third(function<void()> printThird) {
    p2.get_future().wait();
    printThird();
  }
};
```

```go
package main

import "fmt"

var oneDone = make(chan bool)
var twoDone = make(chan bool)

func first() {
  fmt.Println("one")
  oneDone <- true
}

func second() {
  <-oneDone
  fmt.Println("two")
  twoDone <- true
}

func third() {
  <-twoDone
  fmt.Println("three")
}

func main() {
  go second()
  go third()
  go first()

  fmt.Scanln()
}
```

* Synchronized method

```java
class Foo {
  private boolean oneDone;
  private boolean twoDone;

  public Foo() {
    oneDone = false;
    twoDone = false;
  }

  public synchronized void first(Runnable printFirst) throws InterruptedException {
    printFirst.run();
    oneDone = true;
    notifyAll();
  }

  public synchronized void second(Runnable printSecond) throws InterruptedException {
    while (!oneDone) wait();
    printSecond.run();
    twoDone = true;
    notifyAll();
  }

  public synchronized void third(Runnable printThird) throws InterruptedException {
    while (!twoDone) wait();
    printThird.run();
  }
}
```

* Lock

  ```py
  from threading import Lock

  class Foo:
    def __init__(self):
      self.locks = (Lock(),Lock())
      self.locks[0].acquire()
      self.locks[1].acquire()

    def first(self, printFirst):
      printFirst()
      self.locks[0].release()

    def second(self, printSecond):
      with self.locks[0]:
        printSecond()
        self.locks[1].release()

    def third(self, printThird):
      with self.locks[1]:
          printThird()
  ```

* Event

  ```py
  from threading import Event

  class Foo:
    def __init__(self):
      self.done = (Event(),Event())

    def first(self, printFirst):
      printFirst()
      self.done[0].set()

    def second(self, printSecond):
      self.done[0].wait()
      printSecond()
      self.done[1].set()

    def third(self, printThird):
      self.done[1].wait()
      printThird()
  ```
