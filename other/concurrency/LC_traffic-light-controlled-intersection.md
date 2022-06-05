# [LC_traffic-light-controlled-intersection](https://leetcode.com/problems/traffic-light-controlled-intersection)

```en
Given intersection of two roads
First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2
Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4
```

```txt
Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
Output: [
"Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
"Car 3 Has Passed Road A In Direction 1",    // Car 3 crosses the intersection as the light is still green.
"Car 5 Has Passed Road A In Direction 2",    // Car 5 crosses the intersection as the light is still green.
"Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
"Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses the intersection as the light is still green.
]
```

## Solution

* Time; O(n)
* Space; O(1)

* py

  ```py
  import threading

  class TrafficLight(object):
    def __init__(self):
      self.__l = threading.Lock()
      self.__light = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
      """
      :type roadId: int --> // ID of the car
      :type carId: int --> // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
      :type direction: int --> // Direction of the car
      :type turnGreen: method --> // Use turnGreen() to turn light to green on current road
      :type crossCar: method --> // Use crossCar() to make car cross the intersection
      """
      with self.__l:
        if self.__light != roadId:
          self.__light = roadId
          turnGreen()
        crossCar()
  ```
