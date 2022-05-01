# [LC_building-h2o](https://leetcode.com/problems/building-h2o)

Given function that prints h, o. Print hho sequentially

```txt
Input: "OOHHHH"
Output: "HHOHHO"  # "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid
```

## Solution

* cpp

  ```cpp
  class H2O {
    mutex mtxHH, mtxO;
    atomic_int cntH, cntO;
    condition_variable cvO, cvH;
  public:
    H2O() {
      cntH = 0;
      cntO = 0;
    }

    void hydrogen(function<void()> releaseHydrogen) {
      while (cntH == 2) {
        unique_lock<mutex> lck(mtxHH);
        cvH.wait(lck);
      }

      releaseHydrogen();
      cntH++;
      if (cntH == 2 && cntO == 1) {
        cntH = cntO = 0;
        cvO.notify_all();
      }
    }

    void oxygen(function<void()> releaseOxygen) {
      while (cntO == 1) {
        unique_lock<mutex> lck(mtxO);
        cvO.wait(lck);;
      }
      releaseOxygen();
      cntO++;
      if (cntH == 2) {
        cntH = cntO = 0;
        cvH.notify_all();
      }
    }
  };
  ```

* py

  ```py
  from threading import Barrier, Semaphore
  class H2O:
    def __init__(self):
    self.b = Barrier(3)
    self.h = Semaphore(2)
    self.o = Semaphore(1)
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
    self.h.acquire()
    self.b.wait()
    releaseHydrogen()
    self.h.release()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
    self.o.acquire()
    self.b.wait()
    releaseOxygen()
    self.o.release()
  ```
