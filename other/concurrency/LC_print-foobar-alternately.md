# [LC_print-foobar-alternately](https://leetcode.com/problems/print-foobar-alternately)

* en

  ```en
  Print Foo bar alternatively
  ```

* tc

  ```tc
  Input: n = 2
  Output: "foobarfoobar"
  ```

## Solution

* Semaphore

* cpp

  ```cpp
  #include <semaphore.h>
  class FooBar {
  private:
    int n;
    sem_t s1,s2;

  public:
    FooBar(int n) {
      this->n = n;
      sem_init(&s1, 0, 0);
      sem_init(&s2, 0, 1);
    }

    void foo(function<void()> printFoo) {
      for (int i = 0; i < n; i++) {
        sem_wait(&s2);
        printFoo();
        sem_post(&s1);
      }
    }

    void bar(function<void()> printBar) {
      for (int i = 0; i < n; i++) {
        sem_wait(&s1);
        printBar();
        sem_post(&s2);
      }
    }
  };
  ```

* go

  ```go
  package main

  import (
    "fmt"
    "time"
  )

  var (
    signal1 = make(chan struct{})
    signal2 = make(chan struct{})
  )

  func foo(n int) {
    for i := 0; i < n; i++ {
      fmt.Print("foo")
      <-signal2
      signal1 <- struct{}{}
    }
  }

  func bar(n int) {
    for i := 0; i < n; i++ {
      signal2 <- struct{}{}
      fmt.Print("bar")
      <-signal1
    }
  }

  func main() {
    n := 20
    go foo(n)
    go bar(n)
    time.Sleep(time.Second / 2)
  }
  ```

* Monitor

* java

  ```java
  public class FooBarSynchronized {
    private int n;
    private int flag = 0; // flag 0->foo to be print  1->foo has been printed

    public FooBarSynchronized(int n) { this.n = n; }
    public void foo(Runnable printFoo) throws InterruptedException {
      for (int i = 0; i < n; i++) {
        synchronized (this) {
          while (flag == 1) this.wait();
          printFoo.run();
          flag = 1;
          this.notifyAll();
        }
      }
    }

    public void bar(Runnable printBar) throws InterruptedException {
      for (int i = 0; i < n; i++) {
        synchronized (this) {
          while (flag == 0) this.wait();
          printBar.run();
          flag = 0;
          this.notifyAll();
        }
      }
    }
  }
  ```

* Barrior

* py

  ```py
  from threading import Barrier

  class FooBar:
    def __init__(self, n):
      self.n = n
      self.barrier = Barrier(2)

    def foo(self, printFoo):
      for i in range(self.n):
        printFoo()
        self.barrier.wait()

    def bar(self, printBar):
      for i in range(self.n):
        self.barrier.wait()
        printBar()
  ```
