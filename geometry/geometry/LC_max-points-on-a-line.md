# [LC_max-points-on-a-line](https://leetcode.com/problems/max-points-on-a-line)

```en
Given array of points where points[i] = [xi, yi] represents a point on the X-Y plane
Return maximum number of points that lie on the same straight line
```

```txt
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

```

## Solution

* cpp

  ```cpp
  int maxPoints(vector<vector<int>>& points) {
    int res = 1;
    for (int i = 0; i < points.size(); i++) {
      int numVertical = 1, local = 0, duplicate = 0;
      unordered_map<double, int> map;
      for (int j = i + 1; j < points.size() ; j++) {
        if(points[i][0] == points[j][0]) {
          if (points[i][1]==points[j][1]) duplicate++;
          else numVertical++;  // vertical
        } else {
          double slope = (points[i][1]-points[j][1]) / (double)(points[i][0]-points[j][0]);
          map[slope] == 0? map[slope] = 2 : map[slope]++; //If it was zero, add two points!
          local = max(local,map[slope]);
        }
        res = max({res, local + duplicate, numVertical + duplicate});
      }
    }
    return res;
  }
  ```
