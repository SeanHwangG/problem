# [LC_employee-free-time](https://leetcode.com/problems/employee-free-time)

```en
Given list schedule of employees, which represents the working time for each employee
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order
Return list of finite intervals representing common, positive-length free time for all employees, also in sorted order
```

```txt
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
```

## Solution

* py

  ```py
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    iterator = merge(*schedule, key=operator.attrgetter('start'))
    res, prev_end = [], next(iterator).end
    for event in iterator:
      if event.start > prev_end:
        res.append(Interval(prev_end, event.start))
      prev_end = max(prev_end, event.end)
    return res
  ```
