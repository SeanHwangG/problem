# [LC_my-calendar-iii](https://leetcode.com/problems/my-calendar-iii)

* en

  ```en
  K-booking happens when k events have some non-empty intersection (ex: there is some time that is common to all k events)
  Given events [start, end), after each given event, return k representing maximum k-booking between all previous events
  ```

* tc

  ```tc
  Input:
  ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
  [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

  Output: [null, 1, 1, 2, 3, 3, 3]
  ```

## Solution

* cpp

  ```cpp
  map<int, int> count = {{-1, 0}};
  int res = 0;
  MyCalendarThree() {}
  int book(int s, int e) {
    auto start = count.emplace(s, (--count.upper_bound(s))->second);
    auto end = count.emplace(e, (--count.upper_bound(e))->second);
    for (auto i = start.first; i != end.first; ++i)
      res = max(res, ++(i->second));
    return res;
  }
  ```
