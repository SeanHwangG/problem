# [LC_my-calendar-i](https://leetcode.com/problems/my-calendar-i)

```en
Implement a MyCalendar class to store your events
  book(int start, int end). represents a booking on the half open interval [start, end)
Return False if booking is impossible
```

```txt
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
```

## Solution

* py

  ```py
  class MyCalendar:
    def __init__(self):
      self.intervals = []

    def book(self, start : int, end : int) -> bool:
      i = bisect.bisect_right(self.intervals, start)
      j = bisect.bisect_left(self.intervals, end)
      if i % 2 or i != j:  # start is in interval or another interval exists
        return False

      self.intervals[i:i] = [start, end]
      return True
  ```
