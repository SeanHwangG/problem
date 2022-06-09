# [LC_maximum-number-of-visible-points](https://leetcode.com/problems/maximum-number-of-visible-points)

* en

  ```en
  Return max # points you can see with given angle
  ```

* tc

  ```tc
  Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
  Output: 3

  Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
  Output: 4
  ```

## Solution

* py

  ```py
  def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    arr, extra = [], 0
    xx, yy = location
    for x, y in points:
      if x == xx and y == yy:
        extra += 1
        continue
      arr.append(math.atan2(y - yy, x - xx))

    arr.sort()
    arr = arr + [x + 2.0 * math.pi for x in arr]
    angle = math.pi * angle / 180
    l = ans = 0
    for r in range(len(arr)):
      while arr[r] - arr[l] > angle:
        l += 1
      ans = max(ans, r - l + 1)

    return ans + extra
  ```
