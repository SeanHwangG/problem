# [LC_next-closest-time](https://leetcode.com/problems/next-closest-time)

* en

  ```en
  Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits
  There is no limit on how many times a digit can be reused.
  Given string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid
  ```

* tc

  ```tc
  Input: time = "19:34"
  Output: "19:39"

  Input: time = "23:59"
  Output: "22:22"
  ```

## Solution

* py

  ```py
  def nextClosestTime(self, time: str) -> str:
    return min((t <= time, t)
                for i in range(24 * 60)
                for t in ['%02d:%02d' % divmod(i, 60)] if set(t) <= set(time))[1]
  ```
