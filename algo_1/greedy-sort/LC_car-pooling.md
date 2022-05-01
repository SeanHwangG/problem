# [LC_car-pooling](https://leetcode.com/problems/car-pooling)

Vehicle that has capacity empty seats initially available for passengers, which only drives toward east
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about i-th trip
# passengers that must be picked up, and locations to pick up and drop off
Locations are given as the number of kilometers due east from your vehicle's initial location
Return if it is possible to pick up and drop off all passengers for all the given trips

```txt
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

## Solution

* py

  ```py
  def carPooling(self, trips, capacity):
    for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
      capacity -= v
      if capacity < 0:
        return False
    return True
  ```
