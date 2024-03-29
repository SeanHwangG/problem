# [KT_speedlimit](https://open.kattis.com/problems/speedlimit)

* en

  ```en
  Given speed and time, find avergage velocity

  ```

* tc

  ```tc
  Input: 3
  20 2
  30 6
  10 7
  2
  60 1
  30 5
  4
  15 1
  25 2
  30 3
  10 5
  -1

  Output:
  170 miles
  180 miles
  90 miles
  ```

## Solution

* py

  ```py
  def total_miles(speeds, times):
    total_miles = 0
    prev_time = 0
    for speed, time in zip(speeds, times):
      total_miles += (time - prev_time) * speed
      prev_time = time
    return total_miles

  while n_line := int(input()) != -1:
    speeds, times = [], []
    for _ in range(n_line):
      speed, time = map(int, input().split())
      speeds.append(speed)
      times.append(time)
    print(f'{total_miles(speeds, times)} miles')
  ```
