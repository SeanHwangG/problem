# [LC_my-calendar-ii](https://leetcode.com/problems/my-calendar-ii)

* en

  ```en
  Implement a MyCalendar class to store your events
    book(int start, int end). represents a booking on the half open interval [start, end)
  Return False if booking is impossible (event can be added if adding the event will not cause a triple booking)
  ```

* tc

  ```tc
  MyCalendar();
  MyCalendar.book(10, 20); // returns true
  MyCalendar.book(50, 60); // returns true
  MyCalendar.book(10, 40); // returns true
  MyCalendar.book(5, 15);  // returns false
  MyCalendar.book(5, 10);  // returns true
  MyCalendar.book(25, 55); // returns true
  ```

## Solution

* py

  ```py
  # Time; O(n) (Per query) / Space : O(n)
  class MyCalendarTwo:
    def __init__(self):
      self.overlaps, self.calendar = [], []

    def book(self, start, end):
      for i, j in self.overlaps:
        if start < j and end > i:
          return False
      for i, j in self.calendar:
        if start < j and end > i:
          self.overlaps.append((max(start, i), min(end, j)))
      self.calendar.append((start, end))
      return True
  ```
