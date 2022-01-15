{% tabs %}{% tab title='LC_149.cpp' %}

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

{% endtab %}{% endtabs %}
