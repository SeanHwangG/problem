```cpp
class Solution {
public:
  int rectangleArea(vector<vector<int>>& rectangles) {
    set<int> xs, ys;
    for (vector<int> &rect : rectangles) {
      xs.insert({rect[0], rect[2]});
      ys.insert({rect[1], rect[3]});
    }
    vector<int> x(xs.begin(), xs.end()), y(ys.begin(), ys.end());
    vector<vector<bool>> visit(x.size() + 1, vector<bool>(y.size() + 1, false));

    for (vector<int> rect : rectangles){
      int xs = lower_bound(x.begin(), x.end(), rect[0]) - x.begin();
      int xe = lower_bound(x.begin(), x.end(), rect[2]) - x.begin();
      int ys = lower_bound(y.begin(), y.end(), rect[1]) - y.begin();
      int ye = lower_bound(y.begin(), y.end(), rect[3]) - y.begin();
      for (int i = xs; i < xe; i++)
        for (int j = ys; j < ye; j++)
          visit[i][j] = true;
    }

    long ret = 0;
    for (int i = 0; i < x.size(); i++){
      for (int j = 0; j < y.size(); j++){
        if (visit[i][j] && i != x.size() - 1 && j != y.size() - 1)
          ret += (x[i + 1] - x[i]) * (long)(y[j + 1] - y[j]);
    return ret % (long)(1e9 + 7);
  }
};
```
