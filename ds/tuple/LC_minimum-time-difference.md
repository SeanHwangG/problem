# [LC_minimum-time-difference](https://leetcode.com/problems/minimum-time-difference)

* en

  ```en
  Given list of 24-hour clock time point in "HH:MM" format, return min minute difference between any two time-point
  ```

* tc

  ```tc
  Input: timePoints = ["23:59","00:00"]
  Output: 1

  Input: timePoints = ["00:00","23:59","00:00"]
  Output: 0
  ```

## Solution

* py

  ```py
  def findMinDifference(self, timePoints: List[str]) -> int:
    minutes = sorted(list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints)))
    return min((y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1]))
  ```
